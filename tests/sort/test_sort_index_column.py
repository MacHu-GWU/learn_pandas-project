#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import pandas as pd
from learn_pandas import assert_value_equal


def test_sort_index():
    df = pd.DataFrame(
        {"v": [2, 3, 1]},
        index=[2, 3, 1],
    )
    df = df.sort_index(axis=0)
    assert_value_equal(df.index, [1, 2, 3])
    assert_value_equal(df.v, [1, 2, 3])


def test_sort_column():
    df = pd.DataFrame({"b": [2, ], "c": [3, ], "a": [1, ]})
    df.sort_index(axis=1)
    assert_value_equal(df.columns, ["a", "b", "c"])
    assert_value_equal(df.a, [1, ])
    assert_value_equal(df.b, [2, ])
    assert_value_equal(df.c, [3, ])


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
