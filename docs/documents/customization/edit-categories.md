---
sidebar_position: 1
---

# Categories

FlexiMark organizes notes in a hierarchical category structure. This hierarchy can be edited in the `.vscode/settings.json` file of your FlexiMark Workspace.

## How to Change

Open `.vscode/settings.json` and edit the relevant section as shown below. You can use multibyte characters such as Japanese.\
A category without subcategories can be written like `"Life": {}`.

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
