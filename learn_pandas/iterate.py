#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np, pandas as pd
from sfm.timer import Timer

def test_iterate_method_in_pandas():
    """
    
    **测试
    
    """
    p = Path(config.data_dir, "documents_categories.csv")
    with timer.Timer():
        df = pd.read_csv(p.abspath)
    
    with timer.Timer():
        for i, j, k in zip(df["document_id"], df["category_id"], df["confidence_level"]):
            pass
    
    with timer.Timer():
        for i, j, k in zip( *(l for col, l in df.iteritems()) ):
            pass
         
    with timer.Timer():
        for t in df.itertuples():
            ind, i, j, k = t

if __name__ == "__main__":
    test_iterate_method_in_pandas()


        
    
        
