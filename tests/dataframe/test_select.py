#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import pandas as pd
from learn_pandas import assert_value_equal


def test_head_tail():
    data = [[1, 2], [3, 4]]
    df = pd.DataFrame(data)

    assert_value_equal(df.head(1), [[1, 2], ])
    assert_value_equal(df.tail(1), [[3, 4], ])


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
