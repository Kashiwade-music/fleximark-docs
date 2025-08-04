---
sidebar_position: 2
---

# 接頭辞(prefix)と接尾辞(suffix)

FlexiMarkを使ってノートを作成する際、ファイル名の前後にカスタムの文字列を追加できます。固定の文字やいくつかのプレースホルダ―を扱うことができます。

## 変更方法

`.vscode/settings.json`を開き、下記の部分を修正してください。最終的なファイル名は、`{{noteFileNamePrefix}}{{YOUR FILE NAME}}{{noteFileNameSuffix}}.md`となります。\
下記はデフォルトの設定です。この設定だと`20250804_Hello World.md`のようなファイル名になります。

```json title=".vscode/settings.json" {3-4}
{
  ...
  "fleximark.noteFileNamePrefix": "${CURRENT_YEAR}${CURRENT_MONTH}${CURRENT_DATE}_",
  "fleximark.noteFileNameSuffix": "",
  ...
}
```

## 対応するプレースホルダー

以下は、対応記法とそれに対応する意味・出力例をまとめたものです。

| プレースホルダー                  | 意味                                  | 出力例（2025年8月4日 14:05:09 UTC+9想定）    |
| --------------------------------- | ------------------------------------- | -------------------------------------------- |
| `${CURRENT_YEAR}`                 | 西暦（4桁）                           | `2025`                                       |
| `${CURRENT_YEAR_SHORT}`           | 西暦の下2桁                           | `25`                                         |
| `${CURRENT_MONTH}`                | 月（2桁、01～12）                     | `08`                                         |
| `${CURRENT_MONTH_NAME}`           | 月の名称（表示言語に依存）            | `August`, `8月`                              |
| `${CURRENT_MONTH_NAME_ENG}`       | 月名（英語、フル）                    | `August`                                     |
| `${CURRENT_MONTH_NAME_SHORT}`     | 月の略称（表示言語に依存）            | `Aug`, `8月`                                 |
| `${CURRENT_MONTH_NAME_SHORT_ENG}` | 月名（英語、省略）                    | `Aug`                                        |
| `${CURRENT_DATE}`                 | 日（2桁、01～31）                     | `04`                                         |
| `${CURRENT_DAY_NAME}`             | 曜日名（表示言語に依存）              | `Monday`, `月曜日`                           |
| `${CURRENT_DAY_NAME_ENG}`         | 曜日名（英語）                        | `Sunday`                                     |
| `${CURRENT_DAY_NAME_SHORT}`       | 曜日略称（表示言語に依存）            | `Mon`, `月`                                  |
| `${CURRENT_DAY_NAME_SHORT_ENG}`   | 曜日略称（英語）                      | `Sun`                                        |
| `${CURRENT_HOUR}`                 | 時（24時間制、2桁）                   | `14`                                         |
| `${CURRENT_MINUTE}`               | 分（2桁）                             | `05`                                         |
| `${CURRENT_SECOND}`               | 秒（2桁）                             | `09`                                         |
| `${CURRENT_SECONDS_UNIX}`         | UNIXタイムスタンプ（秒）              | `1754306709`                                 |
| `${CURRENT_TIMEZONE_OFFSET}`      | タイムゾーンオフセット（±hhmm形式）   | `+0900`                                      |
| `${RANDOM}`                       | 6桁のランダムな整数（100000〜999999） | `538291`（例）                               |
| `${RANDOM_HEX}`                   | 6桁のランダムな16進数（小文字）       | `a3f92c`（例）                               |
| `${UUID}`                         | UUID（バージョン4）                   | `3f29b260-1e6a-4fc5-a13d-847abf4dd3a1`（例） |

