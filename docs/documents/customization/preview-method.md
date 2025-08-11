---
sidebar_position: 5
---

# How to Preview

You can change the preview method that is triggered when clicking the icon in the top-right corner.

## Overview

FlexiMark allows you to choose whether to preview Markdown in VSCode or in a browser. Each option has its pros and cons, so configure it according to your needs.

```mermaid
flowchart TD
    A{{Is the Markdown file<br>inside the FlexiMark Workspace?}} -->|Yes| B{{Do you want to enable<br>JS or iframe in the Markdown?}}
    A -->|No| D[【In VSCode】<br>User JS is not executed, making it secure.]

    B -->|Yes| C[【In Browser】<br>JS and iframe are both supported.]
    B -->|No| E[【In VSCode】<br>JS is not executed,<br>iframe is not supported.]
```

## How to Change

Open `.vscode/settings.json` and edit the following section. Available values are `vscode` or `browser`. Below is the default setting:

```json title=".vscode/settings.json" {3} 
{
  ...
  "fleximark.defaultPreviewMode": "vscode",
  ...
}
```