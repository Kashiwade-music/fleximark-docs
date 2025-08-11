---
sidebar_position: 3
---

# Template

You can configure a template to use when creating notes.

## How to Change

Open `.vscode/settings.json` and modify the relevant section as shown below. This is the default configuration:
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

Each line of the template should be written as an element in the array.
For example, if you want a template like the one below:

```plaintext
# Title

## Heading 2

```

You should write it like this:

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

VSCode allows you to use placeholders and tab stops. For more details on the available syntax, please refer to the following page:

https://code.visualstudio.com/docs/editing/userdefinedsnippets#_snippet-syntax