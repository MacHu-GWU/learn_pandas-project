#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import pandas as pd
from learn_pandas import assert_value_equal


def test():
    df1 = pd.DataFrame({"v1": [1, ]}, index=[0, ])
    df2 = pd.DataFrame({"v2": [2, ]}, index=[1, ])

    df_concat = pd.concat([df1, df2])
    """
        v1      v2
    0   1       np.nan
    1   np.nan  2
    """

    df_join = df1.join(df2, how="outer")
    """
        v1      v2
    0   1       np.nan
    1   np.nan  2
    """


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
