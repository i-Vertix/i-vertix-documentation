---
title: Markdown Cheat sheet
sidebar_position: 2
---

# Markdown Cheatsheet

## Headings

---

# Use # for the main title

## Use ## for a smaller title

### Use ### for a smaller title

#### Use #### for a smaller title

##### Use ##### for a smaller title

###### Use ###### for a smaller title

---

## Text format

- use `**text**` to create a **bold text**
- use `*text*` or `_text_` to create an _italic text_
- use `**_text_**` to create an **_italic bold text_**
- use \`text\` for `formatting code`

---

## Lists

1. use `1. text` to create a ordered list
2. for the second item use `2. text`
3. for the thrird item use `3. text`
4. and so on

* use `* text` for an unordered list
* obviously use `* text` also for the other items

- [ ] use `[ ] text` to create task lists
- [x] use `[x] text` to check a task

---

## Quotes

> use > if you want to create a quote
>
> it is also possible to start on a new line by adding only a `>` at the start of the line
> otherwise the text will always be appended to the previous line

---

## Code blocks

```text
If you want to create blocks of code you can simply write 
```these characters and then you can write anything you like, 
also writing multiple lines is no problem```
```

---

## Links

> use `[display text](url)` to add a link
>
> in the following example `[i-Vertix Homepage](https://i-vertix.com)` is used

[i-Vertix Homepage](https://i-vertix.com)

> **Note**: if you want to link to an internal documentation page use the following url:
>
> `[Monitoring Intro](/monitoring/intro)`

[Monitoring Intro](/monitoring/intro)

---

## Images

> use `![image description](image url)` to add an image
>
> in the following example `![exmaple image](/img/logo-ivertix-100.png)` is used

![exmaple image](https://i0.wp.com/i-vertix.com/wp-content/uploads/2022/01/cropped-logo_blu_100x100-1.png?fit=101%2C101&ssl=1)

---

## Tables

```text
Creating tables is a little bit tricky

| City | Country | Capital |
| --- | --- | --- |
| Rome | Italy | ✅ |
| Bolzano | Italy | ❌ |
| Berlin | Germany | ✅ |
| Vienna | Austria | ✅ |
```

| City | Country | Capital |
| --- | --- | -- |
| Rome | Italy | ✅ |
| Bolzano | Italy | ❌ |
| Berlin | Germany | ✅ |
| Vienna | Austria | ✅ |

---

## Divider (horizontal line)

use `---` to create a horizontal line to divide sections of your page

---

## Emojis

make use of emojis, they are cool

- [Emoji cheat sheet](https://github.com/ikatyang/emoji-cheat-sheet)
- [Full emoji list](https://unicode.org/emoji/charts/full-emoji-list.html)

> **Note:** Simply copy the desired emoji and paste it inside your markdown file

---

## Special things (only available in documentation software)

### Alerts

```text
:::note

Some **content** with _Markdown_ `syntax`.

:::

:::tip

Some **content** with _Markdown_ `syntax`.

:::

:::info

Some **content** with _Markdown_ `syntax`.

:::

:::caution

Some **content** with _Markdown_ `syntax`.

:::

:::danger

Some **content** with _Markdown_ `syntax`.

:::
```

![Alerts](https://i.imgur.com/Gbl6dBH.png)
