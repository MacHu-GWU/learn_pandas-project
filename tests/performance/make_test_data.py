#!/usr/bin/env python
# -*- coding: utf-8 -*-

data_file_path = __file__.replace("make_test_data.py", "data.csv")

def make_test_data():
    import numpy as np, pandas as pd
    
    df = pd.DataFrame(np.random.random((10000, 4)), columns=list("ABCD"))
    df.to_csv(data_file_path, index=False)
    
if __name__ == "__main__":
    make_test_data()
    
    