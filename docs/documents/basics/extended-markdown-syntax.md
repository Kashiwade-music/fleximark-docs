---
sidebar_position: 2
---

# Markdownの文法（拡張）

FlexiMarkがサポートするMarkdownの拡張文法を紹介します。

## 概要

FlexiMarkは[Markdownの文法（基本）](./basic-markdown-syntax.md)で扱ったものに加えて、独自の拡張記法をサポートしています。これらの記法は広くスタンダートであるとは言えませんが、日常のメモをMarkdownで記録する際に便利だと考えたため、サポートしています。

## 付箋（Admonition/Alert）記法

[DocusaurusのAdmonitions](https://docusaurus.io/docs/markdown-features/admonitions) や [GitHubのAlert](https://docs.github.com/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts) に相当する機能です。ブロック内では各種Markdownの記法を使うことができます。また、後述する[「付箋（Admonition/Alert）の収集」](../feature/collect-admonitions.md)を用いることで、指定カテゴリ以下の全てのノートに存在する付箋（Admonition/Alert）を単一のMarkdownに収集して整理することもできます。

```plaintext
:::info

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

:::

:::tip

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

:::

:::warning

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

:::

:::danger

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

:::
```

![](img/extended-markdown-syntax/00_admonition_alert.png)

付箋（Admonition/Alert）にカスタムタイトルをつけることもできます。タイトルには各種Markdown記法を使うことができます。

```plaintext
:::info[*Custom* ~Title~]

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

:::

:::tip[*Custom* ~Title~]

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

:::

:::warning[*Custom* ~Title~]

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

:::

:::danger[*Custom* ~Title~]

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

:::
```

![](img/extended-markdown-syntax/01_admonition_alert_custom_title.png)

:::tip

付箋（Admonition/Alert）はネストもできますが、`:`の数を変えることでペアを作る書き方がおすすめです。

![](img/extended-markdown-syntax/02_admonition_alert_nested.png)

:::

## タブ記法

タブを作り、内容を分けることができます。ブロック内では各種Markdownの記法を使うことができます。

```plaintext
::::tabs

:::tab[Tab 1]

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

:::

:::tab[Tab 2]

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

:::

::::
```

![](img/extended-markdown-syntax/03_tab.png)

## 折り畳み

HTMLにおける`<details>`タグの代替となる記法です。カスタムタイトルをつけることもできます。

```plaintext
:::details

**Collapsible Section (Click to Expand)**

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

:::

:::details[Custom Title]

**Collapsible Section (After Manual Expansion)**

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

:::
```

![](img/extended-markdown-syntax/04_details.png)


## YouTube iframe

YouTubeのURLが1つの段落として追加された場合、自動でiframeに変換します。短縮URL以外にも対応しています。段落中にYouTubeのURLがあった場合はiframeに変換しません。

```plaintext
https://youtu.be/G1W3aroArqY

Lorem https://youtu.be/G1W3aroArqY dolor sit amet, consectetur adipiscing elit.
```

![](img/extended-markdown-syntax/05_youtube.png)

:::warning

VSCodeのプレビュー上ではiframeは正常に動作しません。iframeを動作させたい場合はブラウザプレビューを利用してください。

:::

## コードブロック

コードブロック内のシンタックスハイライトに加え、タイトル表示、行数表示、行のハイライトに対応しています。

````plaintext
```js
document.body.addEventListener('click', () => {
  const colors = ['blue', 'green', 'pink', 'yellow'];
  const randomColor = colors[Math.floor(Math.random() * colors.length)];
  document.body.style.backgroundColor = randomColor;
});
```

```js title="color.js"
document.body.addEventListener('click', () => {
  const colors = ['blue', 'green', 'pink', 'yellow'];
  const randomColor = colors[Math.floor(Math.random() * colors.length)];
  document.body.style.backgroundColor = randomColor;
});
```

```js title="color.js" showLineNumbers
document.body.addEventListener('click', () => {
  const colors = ['blue', 'green', 'pink', 'yellow'];
  const randomColor = colors[Math.floor(Math.random() * colors.length)];
  document.body.style.backgroundColor = randomColor;
});
```

```js title="color.js" showLineNumbers {1,3-5}
document.body.addEventListener('click', () => {
  const colors = ['blue', 'green', 'pink', 'yellow'];
  const randomColor = colors[Math.floor(Math.random() * colors.length)];
  document.body.style.backgroundColor = randomColor;
});
```
````

![](img/extended-markdown-syntax/06_code_block.png)

## Mermaid

[Mermaid](https://mermaid.js.org)による各種ダイアグラム描画を行うことができます。

````plaintext
```mermaid
sequenceDiagram
    actor Alice
    actor Bob
    Alice->>Bob: Hi Bob
    Bob->>Alice: Hi Alice
```
````

![](img/extended-markdown-syntax/07_mermaid.png)

:::tip

Mermaidのシンタックスハイライトには下記の拡張機能を別途インストールするのがおすすめです。

- [Mermaid Markdown Syntax Highlighting](https://marketplace.visualstudio.com/items?itemName=bpruitt-goddard.mermaid-markdown-syntax-highlighting)

:::

## ABC記譜法

[ABC記譜法](https://abcnotation.com)に対応し、楽譜を書くことができます。また、シンタックスハイライト、各種スニペット、楽譜の再生、カーソル編集位置の表示などにも対応しています。

````plaintext
```abc
X:1
T:Demo Song
C:Kashiwade
M:6/8
L:1/8
K:Bm
Q:1/4=175
%%staves  {(rh) (lh)}
V:rh clef=treble 
V:lh clef=treble
% Start of the melody
[V:rh]
fefcBe | fcBafe | fefcBe | fcBabf |
[V:lh]
G,2D2F2 | G,2D2E2 | G,2D2F2 | G,2D2E2 |
% next line
[V:rh]
edeABd | edeafd | edeABd | [ec]d[fA]B[ec]2 |
[V:lh]
F,2A,2C2 | F,2A,2E2 | F,2A,2C2 | F,2A,2E2 |
%next line
[V:rh]
[fB]efcBe | fcBafe | fefcBe | fcBabd' |
[V:lh]
G,2D2F2 | G,2D2E2 | G,2D2F2 | G,2D2E2 |
%next line
[V:rh]
c'd'caAf | e2dAc2 | c2d2-dA | c2d4 :|
[V:lh]
F,2A,2C2 | F,2C2A2 | B,2D2F2- | FAFEB,2 :|
```
````

![](img/extended-markdown-syntax/08_abc.png)