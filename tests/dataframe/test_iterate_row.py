#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import sys
import pandas as pd
from learn_pandas import Timer

if sys.version_info.major == 2:
    import itertools
    zip = itertools.izip


def test_iterate_row():
    n = 1000000
    l = list(range(n))
    data = {"a": l, "b": l, "c": l}
    df = pd.DataFrame(data)

    with Timer() as timer:
        for i, j, k in zip(*(l for col, l in df.iteritems())):
            pass
    elapse1 = timer.elapse

    with Timer() as timer:
        for i, j, k in zip(df.a, df.b, df.c):
            pass
    elapse2 = timer.elapse

    with Timer() as timer:
        for ind, i, j, k in df.itertuples():
            pass
    elapse3 = timer.elapse

    print(elapse1, elapse2, elapse3)
    # assert elapse1 < elapse2
    # assert elapse2 < elapse3


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
