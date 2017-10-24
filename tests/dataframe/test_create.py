#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import numpy as np, pandas as pd
from learn_pandas import assert_value_equal


def test_from_records():
    data = [[1, 2], [3, 4]]
    df = pd.DataFrame(data, columns=["c1", "c2"], index=["r1", "r2"])
    assert_value_equal(df, data)


def test_from_dict():
    data = {"c1": [1, 3], "c2": [2, 4]}
    df = pd.DataFrame(data, columns=["c1", "c2"], index=["r1", "r2"])
    assert_value_equal(df, [[1, 2], [3, 4]])


def test_from_row_list():
    data = [{"c1": 1, "c2": 2}, {"c1": 3, "c2": 4}]
    df = pd.DataFrame(data, columns=["c1", "c2"], index=["r1", "r2"])
    assert_value_equal(df, [[1, 2], [3, 4]])


def test_timeseries():
    m, n = 2, 3
    data = [[1, 2, 3], [4, 5, 6]]
    df = pd.DataFrame(
        data,
        index=pd.date_range("2017-01-01", periods=m, freq="D"),
        columns=list("ABC")
    )
    assert_value_equal(df, data)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
