#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import pandas as pd
from learn_pandas import assert_value_equal


def test():
    """
    将两个Column相同的DataFrame连接起来，对于有相同的Index，使用 前面/后面 的哪一个。
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

    df = pd.concat([df1, df2])
    assert_value_equal(df.v, [1, 1, 2, 2])
    """
       v
    0  1
    1  1
    1  2
    2  2
    """

    # Remove Duplicate Index, keep df1's
    res = df[~df.index.duplicated(keep="first")]
    assert_value_equal(res.v, [1, 1, 2])
    """
       v
    0  1
    1  1
    2  2
    """

    # Remove Duplicate Index, keep df2's
    res = df[~df.index.duplicated(keep="last")]
    assert_value_equal(res.v, [1, 2, 2])
    """
       v
    0  1
    1  2
    2  2
    """


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
