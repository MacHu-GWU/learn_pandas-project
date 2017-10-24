#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ref:

- https://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html
"""

import pytest
import pandas as pd
from learn_pandas import assert_value_equal


def test():
    df1 = pd.DataFrame({"A": ["A1", ]}, index=[1, ])
    df2 = pd.DataFrame({"A": ["A2", ]}, index=[2, ])

    # concat index
    df = pd.concat([df1, df2], axis=0)
    """
        A
    1   A1
    2   A2
    """
    assert df.shape == (2, 1)

    # concat column
    df = pd.concat([df1, df2], axis=1)
    """
        A   A
    1   A1  Nan
    2   Nan A2
    """
    assert df.shape == (2, 2)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
