#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
import numpy as np
import pandas as pd
from learn_pandas import utils


def test_assert_value_equal():
    values = [[1, 2], [3, 4]]
    df = pd.DataFrame(values)
    utils.assert_value_equal(df, values)
    utils.assert_value_equal(np.array(values), values)
    with raises(AssertionError):
        utils.assert_value_equal(df, [[0, 0], [0, 0]])
    with raises(Exception):
        utils.assert_value_equal(df, [0, 0, 0, 0])


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
