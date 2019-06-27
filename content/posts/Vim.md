Status: published
Date: 2018-10-04 11:23:36 
Author: Jerry Su
Slug: Vim
Title: Vim
Category: Vim
Tags: Vim

[TOC]

## 1st Level - Survive

### Normal mode

- **`i`** → Insert mode. Type **`ESC`** to return to Normal mode.
- **`x`** → Delete the char under the cursor
- **`:wq`** → Save and Quit (**`:w`** save, **`:q`** quit)
- **`dd`** → Delete (and copy) the current line
- **`p`** → Paste

**Recommended:**

- **`hjkl`** (highly recommended but not mandatory) → basic cursor move (←↓↑→). 
- **`:help <command>`** → Show help about **`<command>`**. You can use :help without a **`<command>`** to get general help.

## 2nd Level – Feel comfortable

### Insert mode variations:
 
- **`a`** → insert after the cursor
- **`o`** → insert a new line after the current one
- **`O`** → insert a new line before the current one
- **`cw`** → replace from the cursor to the end of the word

### Basic moves:

- **`0`** → go to the first column
- **`^`** → go to the first non-blank character of the line
- **`$`** → go to the end of column
- **`g_`** → go to the last non-blank character of line
- **`/pattern`** → search for **`pattern`**

### Copy / Paste

- **`P`** → paste before, remember **`p`** is paste after current position.
- **`yy`** → copy the current line, easier but equivalent to **`ddP`**

### Undo / Redo

- **`u`** → undo
- **`<C-r>`** → redo

### Load/Save/Quit/Change File (Buffer)

- **`:e <path/to/file>`** → open
- **`:w`** → save
- **`:saveas <path/to/file>`** → save to **`<path/to/file>`**
- **`:x`**, **`ZZ`** or **`:wq`** → save and quit (**`:x`** only save if necessary)
- **`:q!`** → quit without saving, also: **`:qa!`** to quit even if there are modified hidden buffers.
- **`:bn`** (resp. **`:bp`**) → show next (resp. previous) file (buffer)

## 3rd Level – Better. Stronger. Faster.

### Better

- **`.`** → (dot) will repeat the last command,
- **N`<command>`** → will repeat the command N times.
- **`2dd`** → will delete 2 lines
- **`3p`** → will paste the text 3 times
- **`100idesu [ESC]`** → will write “desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu”
- **`.`** → Just after the last command will write again the 100 “desu”.
- **`3.`** → Will write 3 “desu” (and not 300, how clever).

### Stronger

**Move efficiently with vim is very important!**

- **N`G`** → Go to line N
- **`gg`** → shortcut for 1G - go to the start of the file
- **`G`** → Go to last line

- **<font color=red>Word moves</font>:**
	- **`w`** → go to the start of the following word,
	- **`e`** → go to the end of this word.
	- **`W`** → go to the start of the following WORD,
	- **`E`** → go to the end of this WORD.
	
	By default, words are composed of letters and the underscore character. Let’s call a WORD a group of letter separated by blank characters. If you want to consider WORDS, then just use uppercase characters.
{% asset_img word_moves.jpg %}
	
- **<font color=red>`%`</font>** : Go to the corresponding **`(`**, **`{`**, **`[`**.
- **<font color=red>`*`</font>** (resp. **`#`**) : go to next (resp. previous) occurrence of the word under the cursor

**<font color=red size=4>The last three commands are gold.</font>**

### Faster

Most commands can be used using the following general format:
**`<start position><command><end position>`**
For example : **`0y$`** means
- **`0`** → go to the beginning of this line
- **`y`** → yank from here
- **`$`** → up to the end of this line

We also can do things like **`ye`**, yank from here to the end of the word. But also **`y2/foo`** yank up to the second occurrence of “foo”.
But what was true for **`y`** (yank), is also true for **`d`** (delete), **`v`** (visual select), **`gU`** (uppercase), **`gu`** (lowercase), etc

## 4th Level – Vim Superpowers

### Move on current line: 0 ^ $ g_ f F t T , ;

- **`0`** → go to column 0
- **`^`** → go to first character on the line
- **`$`** → go to the last column
- **`g`**_ → go to the last character on the line
- **`fa`** → go to next occurrence of the letter **`a`** on the line. **`,`** (resp. **`;`**) will find the next (resp. previous) occurrence.
- **`t,`** → go to just before the character **`,`**.
- **`3fa`** → find the 3rd occurrence of **`a`** on this line.
- **`F`** and **`T`** → like **`f`** and **`t`** but backward.

{% asset_img line_moves.jpg %}
A useful tip is: **`dt"`** → remove everything until the **`"`**.

### Zone selection **`<action>a<object>`** or **`<action>i<object>`**

These command can only be used after an operator in visual mode. But they are very powerful. Their main pattern is:

**`<action>a<object>`** and **`<action>i<object>`**

Where action can be any action, for example, **`d`** (delete), **`y`** (yank), **`v`** (select in visual mode). The object can be: **`w`** a word, **`W`** a WORD (extended word), **`s`** a sentence, **`p`** a paragraph. But also, natural character such as **`"`**, **`'`**, **`)`**, **`}`**, **`]`**.

Suppose the cursor is on the first **`o`** of **`(map (+) ("foo"))`**.

- **`vi"`** → will select **`foo`**.
- **`va"`** → will select **`"foo"`**.
- **`vi)`** → will select **`"foo"`**.
- **`va)`** → will select **`("foo")`**.
- **`v2i)`** → will select **`map (+) ("foo")`**
- **`v2a)`** → will select **`(map (+) ("foo"))`**

{% asset_img textobjects.jpg %}

### Select rectangular blocks: **`<C-v>`**.

Rectangular blocks are very useful for commenting many lines of code. Typically: **`0<C-v><C-d>I-- [ESC]`**

- **`^`** → go to the first non-blank character of the line
- **`<C-v>`** → Start block selection
- **`<C-d>`** → move down (could also be jjj or %, etc…)
- **`I-- [ESC]`** → write -- to comment each line

{% asset_img rectangular-blocks.gif %}

Note: in Windows you might have to use **`<C-q>`** instead of **`<C-v>`** if your clipboard is not empty.
