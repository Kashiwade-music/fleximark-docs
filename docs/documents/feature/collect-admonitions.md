# Collecting Admonitions/Alerts

This feature automatically extracts all notes and remarks written using the [Admonition/Alert syntax](../basics/extended-markdown-syntax.md#付箋admonitionalert記法) from every note under a specified category, and compiles them into a single Markdown file. This allows you to organize and view important information scattered across multiple notes by category.

For example, if you have several study notes under a "Mathematics" category, and each note includes sticky notes recording your stumbling points using the Admonition format, you can extract just those notes and reuse them as a "Collection of Stumbling Points in Mathematics." This is useful for review and revisiting information.

![](img/collect-admonitions/00_collect_sample.webp)

## How to Use

With the FlexiMark Workspace open in VSCode, press the `F1` key and enter the following command. Then press `Enter`.

```plaintext
FlexiMark: Collect admonitions/alerts and compile them into a single Markdown file
```
![](img/collect-admonitions/01_input_command.webp)

A category selection dialog will appear. Select the category that contains the notes you want to collect.\
To select an intermediate category, choose the item at the very bottom of the dialog.
![](img/collect-admonitions/02_choose_category.webp)

Finally, enter a file name for the note that will store the collected Admonition/Alert syntax.
![](img/collect-admonitions/03_input_filename.webp)
:::warning

No prefix or suffix will be added to the file name.

:::

The collection process will then be completed.
![](img/collect-admonitions/00_collect_sample.webp)
