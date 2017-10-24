#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import random
import pandas as pd
from learn_pandas import assert_value_equal


def test_sort_index():
    data = [
        [1, 1, 1],
        [1, 2, 2],
        [1, 3, 3],
        [2, 1, 4],
        [2, 2, 5],
        [2, 3, 6],
        [3, 1, 7],
        [3, 2, 8],
        [3, 3, 9],
    ]
    columns = ["k1", "k2", "v"]
    random.shuffle(data)
    df = pd.DataFrame(data, columns=columns)

    res = df.sort_values(["k1", ])
    assert_value_equal(res.k1, [1, 1, 1, 2, 2, 2, 3, 3, 3])
    """
    k1  k2  v
    1   3   3
    1   1   1
    1   2   2
    2   2   5
    2   1   4
    2   3   6
    3   1   7
    3   2   8
    3   3   9
    """

    res = df.sort_values(["k2", ])
    assert_value_equal(res.k2, [1, 1, 1, 2, 2, 2, 3, 3, 3])
    """
    k1  k2  v
    2   1   4
    3   1   7
    1   1   1
    1   2   2
    3   2   8
    2   2   5
    1   3   3
    3   3   9
    2   3   6
    """

    res = df.sort_values(["k1", "k2"])
    assert_value_equal(res.k1, [1, 1, 1, 2, 2, 2, 3, 3, 3])
    assert_value_equal(res.k2, [1, 2, 3, 1, 2, 3, 1, 2, 3])
    """
    k1  k2  v
    1   1   1
    1   2   2
    1   3   3
    2   1   4
    2   2   5
    2   3   6
    3   1   7
    3   2   8
    3   3   9
    """


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
