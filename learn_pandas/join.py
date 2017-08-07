#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.join.html
"""

import pandas as pd

# left = pd.DataFrame({"key": ["k1", "k2", "k3"], "value": [1, 2 ,3]})
# right = pd.DataFrame({"key": ["k2", "k3", "k4"], "value": [4, 5 ,6]})
# print(left.join(right, on="key", how="left", lsuffix="_l", rsuffix="_r"))
# print(left.join(right, on="key", how="outer", lsuffix="_l", rsuffix="_r"))


left = pd.DataFrame([
    ["k1", 1],
    ["k2", 2],
    ["k3", 3],
], columns=["key", "value_l"])

right = pd.DataFrame([
    ["k2", 2],
    ["k3", 3],
    ["k4", 4],
], columns=["key", "value_r"])

print(left.join(right, on=["key",], how="left", ))