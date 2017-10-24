#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import pandas as pd
from learn_pandas import assert_value_equal


def test():
    """
    Update操作是，将新DataFrame中凡是跟原DataFrame的Index和Column有重复的位置，只要
    值不是 np.nan, 就用它取代原DataFrame中的值。

    **此操作只考虑原DataFrame中有的Index和Column**。
    """
    df1 = pd.DataFrame({"v": [1, 1]}, index=[0, 1])
    """
        v
    0   1
    1   1
    """

    df2 = pd.DataFrame({"v": [2, 2]}, index=[1, 2])
    """
        v
    1   2
    2   2
    """

    df = pd.DataFrame({"v": [0, 0, 0]}, index=[0, 1, 2])
    df.update(df1)
    assert_value_equal(df.v, [1, 1, 0])
    """
        v
    0   1
    1   1
    2   0
    """
    df.update(df2)
    assert_value_equal(df.v, [1, 2, 2])
    """
        v
    0   1
    1   2
    2   2
    """


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
