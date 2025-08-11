---
sidebar_position: 4
---

# アセットの保存場所

VSCodeのエディタに張り付けた画像の保存場所を指定できます。

## 概要

VSCodeの機能により、下記の操作で画像の挿入が可能です。

- 画像がクリップボードにある場合はVSCode上で`Ctrl+V`
- `Shift`キーを押しながら画像をVSCodeのテキストエディタ上にドラッグ&ドロップ

デフォルトの設定では、`./attachments`フォルダ以下にノートのカテゴリと同じ階層の位置に保存されます。\
例えば、`Tips/Life/Hello World.md`に`image.png`を貼り付けた場合、画像は`attachments/Tips/Life/Hello World`以下に保存されます。

```plaintext
<<FlexiMark Workspace>>
├── Tips
│   └── Life
│       └── Hello World.md     <- using image.png
└── attachments
    └── Tips
        └── Life
            └── Hello World
                └── image.png  <- saved here
```

## 変更方法

`.vscode/settings.json`を開き、下記の部分を修正してください。下記はデフォルトの設定です。
```json title=".vscode/settings.json" {3-5} 
{
  ...
  "markdown.copyFiles.destination": {
    "**/*.md": "${documentWorkspaceFolder}/attachments/${documentRelativeDirName}/${documentBaseName}/"
  },
  ...
}
```

詳細はVSCodeの下記のドキュメントを参照してください。

https://code.visualstudio.com/updates/v1_79#_markdowncopyfilesdestination