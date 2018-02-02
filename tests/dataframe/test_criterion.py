#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import numpy as np
import pandas as pd
from learn_pandas import Timer


def test_lambda():
    """
    Complex select rows by values.
    """
    df = pd.DataFrame([[1, 1], [2, 2], [3, 3], [4, 4]], columns=list("AB"))
    crt = df.A.map(lambda x: 2 <= x <= 3)
    df = df[crt]
    assert (df.values == [
        [2, 2],
        [3, 3],
    ]).all()


def test_performance():
    """
    Test different way of doing row selection.
    """
    df = pd.DataFrame(np.random.random((50000, 4)), columns=list("ABCD"))

    with Timer() as timer:
        df1 = df[(df.A >= 0.25) & (df.A <= 0.75)] # Preferred
    elapse1 = timer.elapse

    with Timer() as timer:
        crt = df.A.map(lambda x: 0.25 <= x <= 0.75) # More powerful but slower
        df2 = df[crt]
    elapse2 = timer.elapse

    assert (df1 == df2).values.all()
    assert elapse1 < elapse2


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
