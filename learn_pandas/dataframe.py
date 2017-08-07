#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np, pandas as pd
from sfm.decorator import run_if_is_main

@run_if_is_main(__name__)
def construct_dataframe():
    # from records
    data = [[1, 2], [3, 4]]
    df1 = pd.DataFrame(data, columns=["c1", "c2"], index=["r1", "r2"])
    
    # from dict
    data = {"c1": [1, 3], "c2": [2, 4]}
    df2 = pd.DataFrame(data, columns=["c1", "c2"], index=["r1", "r2"])
    
    # from items
    data = [{"c1": 1, "c2": 2}, {"c1": 3, "c2": 4}]
    df3 = pd.DataFrame(data, columns=["c1", "c2"], index=["r1", "r2"])
    
construct_dataframe()

@run_if_is_main(__name__)
def test():
    df = pd.DataFrame(np.random.rand(6, 4), columns=list("abcd"))
    print(df.head(3)) # first 3 rows
    print(df.tail(3)) # last 3 rows
    print(df.describe()) # count, mean, std, min, max, 25%, 50%, 75%
    
# test()

@run_if_is_main(__name__)
def timeseries():
    import string
    
    m, n = 6, 4
    df = pd.DataFrame(np.random.rand(m, n))
    df.columns = list(string.ascii_lowercase[:n])
    df.index = pd.date_range("2017-01-01", periods=m, freq="D")
    
    print(df.first("3D")) # first 3 day
    print(df.last("3D")) # last 3 day

# timeseries()