#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import tablib
import pandas as pd
from make_test_data import data_file_path
from sfm.timer import Timer

def test():
    with Timer(title="pandas") as timer:
        df = pd.read_csv(data_file_path)
    elapse_pandas = timer._elapsed
    
    with Timer(title="tablib") as timer:
        data = tablib.Dataset().load(open(data_file_path).read())
    elapse_tablib = timer._elapsed
    
    assert elapse_pandas < elapse_tablib
         
if __name__ == "__main__":
    import os
    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])