date: 2021-01-04 10:17:17
author: Jerry Su
slug: Python-typing
title: Python - typing
category: 
tags: Python
summary: Reason is the light and the light of life.
toc: show


```python
from typing import Union, Optional, Callable, Iterable, Mapping, Sequence, List, Tuple, Any
```

[https://docs.python.org/3/library/typing.html](https://docs.python.org/3/library/typing.html)

Any, Union, Tuple, List, Sequence, Mapping, Callable, TypeVar,Optional, Generic等的使用频率比较高，其中Union、Optional、Sequence、Mapping非常有用。

- Union

即并集，所以Union[X, Y] 意思是要么X类型、要么Y类型

- Optional

Optional[X]与Union[X, None]，即它默认允许None类型

- Sequence

即序列，需要注意的是，List一般用来标注返回值；Sequence、Iterable用来标注参数类型

- Mapping

即字典，需要注意的是，Dict一般用来标注返回值；Mapping用来标注参数类型


```python
def test(
    X: Optional[Union[np.ndarray, pd.DataFrame]] = None,
    obs: Optional[Union[pd.DataFrame, Mapping[str, Iterable[Any]]]] = None,
    var: Optional[Union[pd.DataFrame, Mapping[str, Iterable[Any]]]] = None,
    uns: Optional[Mapping[str, Any]] = None,
    obsm: Optional[Union[np.ndarray, Mapping[str, Sequence[Any]]]] = None,
    varm: Optional[Union[np.ndarray, Mapping[str, Sequence[Any]]]] = None,
    layers: Optional[Mapping[str, Union[np.ndarray, sparse.spmatrix]]] = None,
    raw: Optional[Raw] = None,
    dtype: Union[np.dtype, str] = 'float32',
    shape: Optional[Tuple[int, int]] = None,
    filename: Optional[PathLike] = None,
    filemode: Optional[str] = None,
    asview: bool = False,
    *, oidx: Index = None, vidx: Index = None) -> List[Any]:
    pass
```
