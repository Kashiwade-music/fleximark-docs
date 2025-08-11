---
sidebar_position: 4
---

# Asset Save Location

You can specify where images pasted into the VSCode editor are saved.

## Overview

VSCode allows you to insert images using the following methods:

- Press `Ctrl+V` when an image is in the clipboard
- Drag and drop an image onto the VSCode text editor while holding the `Shift` key

By default, images are saved in the `./attachments` folder, in a path that mirrors the note's category structure.\
For example, if you paste `image.png` into `Tips/Life/Hello World.md`, the image will be saved under `attachments/Tips/Life/Hello World`.

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

## How to Change

Open `.vscode/settings.json` and modify the section below. The following is the default setting:

```json title=".vscode/settings.json" {3-5} 
{
  ...
  "markdown.copyFiles.destination": {
    "**/*.md": "${documentWorkspaceFolder}/attachments/${documentRelativeDirName}/${documentBaseName}/"
  },
  ...
}
```

For more details, refer to the following VSCode documentation:

https://code.visualstudio.com/updates/v1_79#_markdowncopyfilesdestination
