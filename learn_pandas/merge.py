#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.join.html
"""

import pandas as pd

def merge_on_column():
    left = pd.DataFrame([
        ["k1", 1],
        ["k2", 2],
        ["k3", 3],
    ], columns=["key", "value"])
    
    right = pd.DataFrame([
        ["k2", 2],
        ["k3", 3],
        ["k4", 4],
    ], columns=["key", "value"])
    
    assert left.merge(right, how="left", on="key")["key"].tolist() == ["k1", "k2", "k3"]
    assert left.merge(right, how="right", on="key")["key"].tolist() == ["k2", "k3", "k4"]
    assert left.merge(right, how="inner", on="key")["key"].tolist() == ["k2", "k3"]
    assert left.merge(right, how="outer", on="key")["key"].tolist() == ["k1", "k2", "k3", "k4"]

if __name__ == "__main__":
    #
    merge_on_column()
    
def merge_on_multiple_column():
    left = pd.DataFrame([
        ["k1", "k1", 1],
        ["k2", "k2", 2],
        ["k3", "k3", 3],
    ], columns=["key1", "key2", "value"])
    
    right = pd.DataFrame([
        ["k1", "k3", 2],
        ["k2", "k2", 3],
        ["k3", "k1", 4],
    ], columns=["key1", "key2", "value"])
    
    assert left.merge(right, how="left", on=["key1", "key2"])[["key1", "key2"]].values.tolist() == [
        ["k1", "k1"],
        ["k2", "k2"],
        ["k3", "k3"],
    ]
    assert left.merge(right, how="right", on=["key1", "key2"])[["key1", "key2"]].values.tolist() == [
        ["k2", "k2"],
        ["k1", "k3"],
        ["k3", "k1"],
    ]
    assert left.merge(right, how="inner", on=["key1", "key2"])[["key1", "key2"]].values.tolist() == [
        ["k2", "k2"],
    ]
    assert left.merge(right, how="outer", on=["key1", "key2"])[["key1", "key2"]].values.tolist() == [
        ["k1", "k1"],
        ["k2", "k2"],
        ["k3", "k3"],
        ["k1", "k3"],
        ["k3", "k1"],
    ]

    
if __name__ == "__main__":
    #
    merge_on_multiple_column()