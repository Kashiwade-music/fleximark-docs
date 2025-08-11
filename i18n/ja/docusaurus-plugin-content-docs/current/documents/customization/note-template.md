---
sidebar_position: 3
---

# テンプレート

ノートを作成する際のテンプレートを設定することができます。

## 変更方法

`.vscode/settings.json`を開き、下記の部分を修正してください。下記はデフォルトの設定です。
```json title=".vscode/settings.json" {3-11} 
{
  ...
  "fleximark.noteTemplates": {
    "default": [
      "# ${1:first tabstop}",
      "Note Created: ${CURRENT_YEAR}-${CURRENT_MONTH}-${CURRENT_DATE}",
      "",
      "## ${2:second tabstop}"
    ],
    "Template 2": ["# Title", "## Subtitle", "### Subsubtitle"]
  },
  ...
}
```

テンプレートの1行を、1つの配列の要素として記述してください。
例えば下記のようなテンプレートを用意したい場合は次のように記述します。

```plaintext
# Title

## Heading 2

```

```json title=".vscode/settings.json"
{
  ...
  "fleximark.noteTemplates": {
    "sample template": [
      "# Title",
      "",
      "## Heading 2",
      ""
    ],
  },
  ...
}
```

VSCodeの機能により、プレースホルダやタブストップを設定することができます。使うことのできる文法は下記のページを参照してください。

https://code.visualstudio.com/docs/editing/userdefinedsnippets#_snippet-syntax