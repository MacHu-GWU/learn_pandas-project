#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import pandas as pd
from learn_pandas import assert_value_equal

data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9], ]
index = [1, 2, 3]
columns = list("ABC")
df = pd.DataFrame(data, index=index, columns=columns)


def test_specified_row():
    # select second row, use .iloc (Integer Index Only)
    row2 = df.iloc[1]  # the seconds index
    assert_value_equal(row2, [4, 5, 6])
    assert isinstance(row2, pd.Series)

    # select second row, use .loc (Value Index)
    row2 = df.loc[2]  # the index value is 2
    assert_value_equal(row2, [4, 5, 6])
    assert isinstance(row2, pd.Series)


def test_multiple_row():
    # select second and third rows
    row23 = df.iloc[1:3]
    assert_value_equal(row23, [[4, 5, 6], [7, 8, 9]])
    assert isinstance(row23, pd.DataFrame)

    # select second and third rows
    row23 = df.loc[2:3]
    assert_value_equal(row23, [[4, 5, 6], [7, 8, 9]])
    assert isinstance(row23, pd.DataFrame)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
