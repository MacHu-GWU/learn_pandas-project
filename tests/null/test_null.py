#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

import pytest
import pandas as pd
from learn_pandas import assert_value_equal

def test():
    df = pd.DataFrame(
        [[1,    2,    None],
         [None, 5,    6],
         [7,    8,    9],]
    )
    assert_value_equal(
        df.isnull(),
        [[False, False, True],
         [True, False, False],
         [False, False, False],]
    )
    # any na value
    assert df.isnull().values.any() == True

    # for each column, any na in each column
    assert_value_equal(df.isnull().any(axis=0), [True, False, True])

    # for each row, any na in each row
    assert_value_equal(df.isnull().any(axis=1), [True, True, False])


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
