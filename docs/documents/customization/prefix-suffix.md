---
sidebar_position: 2
---

# Prefixes and Suffixes

When creating notes with FlexiMark, you can add custom strings to the beginning and end of the file name. Both fixed text and certain placeholders are supported.

## How to Change

Open `.vscode/settings.json` and edit the relevant part as shown below. The final file name will follow this format: `{{noteFileNamePrefix}}{{YOUR FILE NAME}}{{noteFileNameSuffix}}.md`  
Below is the default setting, which results in a file name like `20250804_Hello World.md`.

```json title=".vscode/settings.json" {3-4}
{
  ...
  "fleximark.noteFileNamePrefix": "${CURRENT_YEAR}${CURRENT_MONTH}${CURRENT_DATE}_",
  "fleximark.noteFileNameSuffix": "",
  ...
}
```

## Supported Placeholders

The table below lists the supported placeholder formats, their meanings, and example outputs (based on the assumption that the date and time is August 4, 2025, 14:05:09 UTC+9).

| Placeholder                       | Meaning                                  | Example Output                                 |
| --------------------------------- | ---------------------------------------- | ---------------------------------------------- |
| `${CURRENT_YEAR}`                 | Four-digit year                          | `2025`                                         |
| `${CURRENT_YEAR_SHORT}`           | Last two digits of the year              | `25`                                           |
| `${CURRENT_MONTH}`                | Month (two digits, 01–12)                | `08`                                           |
| `${CURRENT_MONTH_NAME}`           | Month name (based on display language)   | `August`, `8月`                                |
| `${CURRENT_MONTH_NAME_ENG}`       | Full month name in English               | `August`                                       |
| `${CURRENT_MONTH_NAME_SHORT}`     | Abbreviated month name (locale-based)    | `Aug`, `8月`                                   |
| `${CURRENT_MONTH_NAME_SHORT_ENG}` | Abbreviated month name in English        | `Aug`                                          |
| `${CURRENT_DATE}`                 | Day of the month (two digits, 01–31)     | `04`                                           |
| `${CURRENT_DAY_NAME}`             | Day name (based on display language)     | `Monday`, `月曜日`                             |
| `${CURRENT_DAY_NAME_ENG}`         | Day name in English                      | `Sunday`                                       |
| `${CURRENT_DAY_NAME_SHORT}`       | Abbreviated day name (locale-based)      | `Mon`, `月`                                    |
| `${CURRENT_DAY_NAME_SHORT_ENG}`   | Abbreviated day name in English          | `Sun`                                          |
| `${CURRENT_HOUR}`                 | Hour (24-hour format, two digits)        | `14`                                           |
| `${CURRENT_MINUTE}`               | Minute (two digits)                      | `05`                                           |
| `${CURRENT_SECOND}`               | Second (two digits)                      | `09`                                           |
| `${CURRENT_SECONDS_UNIX}`         | UNIX timestamp (in seconds)              | `1754306709`                                   |
| `${CURRENT_TIMEZONE_OFFSET}`      | Timezone offset (in ±hhmm format)        | `+0900`                                        |
| `${RANDOM}`                       | 6-digit random integer (100000–999999)   | `538291` (example)                             |
| `${RANDOM_HEX}`                   | 6-digit random hexadecimal (lowercase)   | `a3f92c` (example)                             |
| `${UUID}`                         | UUID (version 4)                         | `3f29b260-1e6a-4fc5-a13d-847abf4dd3a1` (example) |
