#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import pandas as pd
from learn_pandas import assert_value_equal


def test_dropna():
    data = [[1, 2, 3],
            [None, 5, 6],
            [7, 8, 9]]
    df = pd.DataFrame(
        data,
        index=[1, 2, 3],
        columns=list("ABC"),
    )
    res = df.dropna(axis=0)  # by row
    assert_value_equal(res, [[1, 2, 3], [7, 8, 9]])
    """
        A   B   C
    1   1   2   3
    3   7   8   9
    """

    res = df.dropna(axis=1)  # by column
    assert_value_equal(res, [[2, 3], [5, 6], [8, 9]])
    """
        B   C
    1   2   3
    2   5   6
    3   8   9
    """


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
