date: 2022-12-16 10:17:17
author: Jerry Su
slug: Brackets-Matching
title: Brackets Matching
category: 
tags: Algorithm
summary: Reason is the light and the light of life.
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


```python
!jupyter nbconvert --to markdown 2022-12-16-Brackets-Matching.ipynb
```

    [NbConvertApp] WARNING | Config option `kernel_spec_manager_class` not recognized by `NbConvertApp`.
    [NbConvertApp] Converting notebook 2022-12-16-Brackets-Matching.ipynb to markdown
    [NbConvertApp] Writing 1800 bytes to 2022-12-16-Brackets-Matching.md



```python

```
