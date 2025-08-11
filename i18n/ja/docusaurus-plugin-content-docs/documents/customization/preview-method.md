---
sidebar_position: 5
---

# プレビューの方法

右上のアイコンをクリックしたときのプレビュー方法を変更できます。

## 概要

FlexiMarkではMarkdownのプレビューをVSCode上とブラウザのどちらで行うのか選択できます。どちらも一長一短なので、用途に合わせて設定してください。

```mermaid
flowchart TD
    A{{Markdownファイルは<br>FlexiMark Workspace内か？}} -->|Yes| B{{MarkdownにJSやiframeがある際<br>それを動作させたいか？}}
    A -->|No| D[【VSCode上】<br>ユーザーのJSは実行されず、セキュリティ上安全。]

    B -->|Yes| C[【ブラウザ】<br>JSもiframeも動作する。]
    B -->|No| E[【VSCode上】<br>JSは実行されず、<br>iframeは動作しない。]
```

## 変更方法

`.vscode/settings.json`を開き、下記の部分を修正してください。取り得る値は`vscode`か`browser`です。下記はデフォルトの設定です。
```json title=".vscode/settings.json" {3} 
{
  ...
  "fleximark.defaultPreviewMode": "vscode",
  ...
}
```