Status: published
Date: 2019-04-12 02:05:45
Author: Jerry Su
Slug: Checking-DataFrame/Series-missing-values
Title: Checking DataFrame/Series missing values
Category: 
Tags: Python
summary: Reason is the light and the light of life.
toc: show

## Checking DataFrame missing values
`cols_missing = frame.columns[frame.isna().any()]`
![asset_img missing_value](images/Checking-DataFrame-Series-missing-values/missing_value.jpg)

## Checking Series missing values
`series.isna().any()`

## has_missing method
```python
from loguru import logger
import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.series import Series
import traceback


def has_missing(self, values):
    """Check whether values have missing value.
    """
    if isinstance(values, DataFrame):
        cols_missing = values.columns[values.isna().any()]
        if not cols_missing.empty:
            logger.warning(f'The columns {", ".join(cols_missing)} contain missing values!' +
                           ''.join(traceback.format_stack()))
        return
    if isinstance(values, Series):
        if values.isna().any():
            logger.warning(f'The {Series.name} Series contain missing values! \n' +
                           ''.join(traceback.format_stack()))
        return
    raise ValueError('The argument values requires a DataFrame or a Series.')
```