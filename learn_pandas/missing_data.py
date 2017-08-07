#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np, pandas as pd


def dropna_example():
    m, n = (6, 4)
    df = pd.DataFrame(np.random.random((m, n)),
        index=["r%s" % i for i in range(m)],
        columns=["c%s" % i for i in range(n)],
    )
    df.loc["r1", "c2"] = None
    df.loc["r3", "c1"] = None
    
    print(df.dropna(axis=0)) # by row
    print(df.dropna(axis=1)) # by column
    
    print(df.dropna(axis=0, subset=["c1",])) # if column c1 is missing, drop the row
    print(df.dropna(axis=0, subset=["c2",])) # if column c2 is missing, drop the row
    
    print(np.isnan(df.loc["r1", "c2"]))
    print(np.isnan(None))
    
    
dropna_example()    
