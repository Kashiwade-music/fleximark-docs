#!/usr/bin/env python3
"""
md_img_convert.py

Recursively scan all Markdown files under the specified directory, parse referenced image files,
convert them to lossless WebP using ffmpeg, update the links in the Markdown files, and delete
the original image files after backing them up.

Example usage:
    python md_img_convert.py --source ./content --backup ./backup_images

Features:
 - Handles inline image links (e.g., ![alt](path/to/img.png "title")).
 - Skips URL references (http:// or https://).
 - Skips files already in .webp format.
 - Supports both relative and absolute paths.
 - Only updates the Markdown if conversion is successful.

Notes:
 - Does not handle reference-style definitions or images embedded with HTML tags.
 - Requires ffmpeg installed and available in PATH.
"""

from __future__ import annotations

import argparse
import logging
import os
import re
import shlex
import shutil
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple

FFMPEG_DEFAULT_OPTS = ["-c:v", "libwebp", "-lossless", "1"]

IMG_LINK_RE = re.compile(r"!\[[^\]]*\]\((<?)([^)\s>]+)(>?)[^)]*\)")

SKIP_EXTS = {".webp"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".tiff", ".bmp", ".avif"}

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("md_webp_convert")


def find_markdown_files(source_dir: Path) -> List[Path]:
    results = []
    for p in source_dir.rglob("*"):
        if p.is_file() and p.suffix.lower() in {".md", ".markdown"}:
            results.append(p)
    return results


def extract_image_paths_from_md(md_text: str) -> List[Tuple[str, int]]:
    matches: List[Tuple[str, int]] = []
    for m in IMG_LINK_RE.finditer(md_text):
        img_path = m.group(2)
        start = m.start(2)
        matches.append((img_path, start))
    return matches


def is_url(path_str: str) -> bool:
    return path_str.startswith(("http://", "https://"))


def should_skip_file(path: Path) -> bool:
    return path.suffix.lower() in SKIP_EXTS


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def copy_to_backup(original: Path, source_root: Path, backup_root: Path) -> Path:
    try:
        rel = original.relative_to(source_root)
    except Exception:
        rel = Path(original.name)
    dest = backup_root / rel
    ensure_dir(dest.parent)
    shutil.copy2(original, dest)
    logger.debug(f"Copied backup {original} -> {dest}")
    return dest


def convert_image_to_webp(src: Path, dst: Path, ffmpeg_path: str = "ffmpeg") -> bool:
    ensure_dir(dst.parent)
    cmd = [ffmpeg_path, "-y", "-i", str(src)] + FFMPEG_DEFAULT_OPTS + [str(dst)]
    logger.debug("Running: %s" % shlex.join(cmd))
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info(f"Converted: {src} -> {dst}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"ffmpeg failed for {src}: {e.stderr.decode(errors='ignore')}")
        return False


def replace_paths_in_markdown(md_text: str, replacements: List[Tuple[str, str]]) -> str:
    for old, new in sorted(replacements, key=lambda x: -len(x[0])):
        md_text = md_text.replace(old, new)
    return md_text


def resolve_image_path(ref_path: str, md_file: Path) -> Optional[Path]:
    p = Path(ref_path)
    if p.is_absolute():
        return p if p.exists() else None
    candidate = (md_file.parent / p).resolve()
    return candidate if candidate.exists() else None


def process_markdown_file(
    md_path: Path, source_root: Path, backup_root: Path, ffmpeg_path: str
) -> None:
    logger.info(f"Processing markdown: {md_path}")
    text = md_path.read_text(encoding="utf-8")
    imgs = extract_image_paths_from_md(text)
    if not imgs:
        logger.debug("No images found.")
        return
    replacements: List[Tuple[str, str]] = []
    for img_ref, _ in imgs:
        if is_url(img_ref):
            logger.debug(f"Skipping URL image: {img_ref}")
            continue
        resolved = resolve_image_path(img_ref, md_path)
        if resolved is None:
            logger.warning(f"Image not found: {img_ref} (in {md_path})")
            continue
        if should_skip_file(resolved):
            logger.debug(f"Skipping excluded file: {resolved}")
            continue
        if resolved.suffix.lower() not in IMAGE_EXTS:
            logger.debug(f"Skipping non-image: {resolved}")
            continue
        try:
            copy_to_backup(resolved, source_root, backup_root)
        except Exception as e:
            logger.error(f"Backup failed {resolved}: {e}")
            continue
        webp_path = resolved.with_suffix(".webp")
        if not convert_image_to_webp(resolved, webp_path, ffmpeg_path=ffmpeg_path):
            logger.error(f"Conversion failed: {resolved}")
            continue
        try:
            new_rel = os.path.relpath(webp_path, start=md_path.parent)
        except Exception:
            new_rel = str(webp_path)
        new_rel = new_rel.replace("\\", "/")
        replacements.append((img_ref, new_rel))
        try:
            resolved.unlink()
            logger.info(f"Deleted original image: {resolved}")
        except Exception as e:
            logger.error(f"Failed to delete original image {resolved}: {e}")
    if replacements:
        md_path.write_text(
            replace_paths_in_markdown(text, replacements), encoding="utf-8"
        )
        logger.info(f"Updated markdown: {md_path}")
    else:
        logger.debug("No replacements performed.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert images in Markdown to lossless WebP, update links, and delete originals."
    )
    parser.add_argument(
        "--source",
        "-s",
        required=True,
        help="Root directory to scan for Markdown files",
    )
    parser.add_argument(
        "--backup",
        "-b",
        required=True,
        help="Directory to store backups of original images",
    )
    parser.add_argument("--ffmpeg", default="ffmpeg", help="Path to ffmpeg executable")
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    source_root = Path(args.source).resolve()
    backup_root = Path(args.backup).resolve()
    if not source_root.exists():
        logger.error(f"Source directory does not exist: {source_root}")
        return
    ensure_dir(backup_root)
    md_files = find_markdown_files(source_root)
    logger.info(f"Found {len(md_files)} markdown files under {source_root}")
    for md in md_files:
        try:
            process_markdown_file(md, source_root, backup_root, ffmpeg_path=args.ffmpeg)
        except Exception as e:
            logger.exception(f"Error processing {md}: {e}")


if __name__ == "__main__":
    main()
