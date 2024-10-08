date: 2022-12-16 10:17:17
author: Jerry Su
slug: Brackets-Matching
title: Brackets Matching
category: 
tags: Algorithm
toc: show


```python
brackets = {')': '(', '》': '《', '）': '（'}
brackets_open, brackets_close = brackets.values(), brackets.keys()


def brackets_match(text: str) -> int:
    """Brackets Match
    """
    stack, error = [], []
    for idx, char in enumerate(text):
        if char in brackets_open:
            stack.append((idx, char))
        elif char in brackets_close:
            if stack and stack[-1][-1] == brackets[char]:
                stack.pop()
            else:
                error.append(idx)
    if stack:
        error = [item[0] for item in stack] + error
    return error
```
