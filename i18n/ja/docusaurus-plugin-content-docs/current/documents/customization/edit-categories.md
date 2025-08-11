---
sidebar_position: 1
---

# カテゴリ

FlexiMarkではノートをカテゴリの階層構造で整理します。カテゴリの階層構造はFlexiMark Workspaceの`.vscode/settings.json`で編集できます。

## 変更方法

`.vscode/settings.json`を開き、下記の部分を修正してください。日本語などの2バイト文字も可能です。\
子カテゴリを持たないカテゴリは`"Life": {}`のように記述できます。

```json title=".vscode/settings.json" {8-18}
{
  "fleximark.settingsVersion": 1,
  // Notes are organized by category.
  // You can add as many categories as needed.
  // Categories are structured as a tree.
  // Notes are saved according to this category structure.
  "fleximark.noteCategories": {
    "General": {
      "Daily Notes": {},
      "Progress Report": {}
    },
    "Tips": {
      "Programming": {
        "Python": {},
        "JavaScript": {}
      },
      "Life": {}
    }
  },
  ...
```
