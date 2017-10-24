#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Join操作是将df1, df2的多个Column按照Index连接起来。在结果里Column是df1, df2都有Column
的合集。

ref: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.join.html
"""

import pytest
import pandas as pd
from learn_pandas import assert_value_equal


def test():
    left = pd.DataFrame({"left": ["left0", "left1"]}, index=[0, 1])
    """
        left
    0   left0
    1   left1
    """

    right = pd.DataFrame({"right": ["right1", "right2"]}, index=[1, 2])
    """
        right
    1   right1
    2   right2
    """

    df = left.join(right, how="left")
    """
        left    right
    0   left0   NaN
    1   left1   righ1
    """

    df = left.join(right, how="right")
    """
        left    right
    1   left1   right1
    2   NaN     right2
    """

    df = left.join(right, how="inner")
    """
        left    right
    1   left1   right1
    """

    df = left.join(right, how="outer")
    """
        left    right
    0   left0   NaN
    1   left1   right1
    2   NaN     right2
    """


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
