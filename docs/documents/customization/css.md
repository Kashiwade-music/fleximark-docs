---
sidebar_position: 6
---

# CSS

FlexiMark allows you to freely customize the style of the preview screen.

## Overview

The appearance during preview is determined by the following three types of CSS:

1. Global CSS  
2. Workspace CSS  
3. `<style>` tags within Markdown files  

Workspace CSS overrides Global CSS, allowing you to change only specific styles if needed.

## How to Change

### Global CSS

Press the `F1` key and enter the following command. Then press `Enter`.

```plaintext
FlexiMark: Open Workspace CSS
```

![](img/css/00_command_global.webp)

This will open the Global CSS in preview mode. You can edit this file to modify the styles.

![](img/css/01_gen_global_css.webp)

### Workspace CSS

Press the `F1` key and enter the following command. Then press `Enter`.

```plaintext
FlexiMark: Open Global CSS
```

![](img/css/02_command_workspace.webp)

This will create a file called `.fleximark/fleximark.css` in your workspace.  
![](img/css/03_gen_workspace_css.webp)

By editing this file, you can change the styles. For example, if you want to make the headings red, you can write:

```css title=".fleximark/fleximark.css" {9-16}
/* 
 * This file is used to override default styles.
 * Default styles are located at:
 * c:\Users\   \AppData\Roaming\Code\User\globalStorage\kashiwade.fleximark\fleximark.css
 * 
 * Please edit this file to customize fleximark appearance.
 */

.markdown-body h1,
.markdown-body h2,
.markdown-body h3,
.markdown-body h4,
.markdown-body h5,
.markdown-body h6 {
  color: red;
}
```

After saving this setting, open any Markdown file and the headings will appear in red.

![](img/css/04_css_change_example.webp)

:::tip

In FlexiMark’s preview, all HTML elements are wrapped inside a `<div class="markdown-body">`.  
So it’s recommended to scope your CSS using `.markdown-body`.

:::

:::warning

To reflect CSS changes in the preview, you need to reload the preview screen.  
Press the `F1` key and enter the following command. Then press `Enter`.

```plaintext
FlexiMark: Force Reload Preview
```

:::