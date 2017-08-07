#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
update能将一个DataFrame中的NA值用另一个DataFrame中的数值填补。有的时候也可以用

ref: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.update.html
"""

import numpy as np
import pandas as pd
from pytest import approx


def test_update():
    """
    
    **中文文档**
    
    update方法默认将所有bool()为False的值进行替换
    """
    df1 = pd.DataFrame(np.zeros((4, 4)))
    df2 = pd.DataFrame(np.random.randn(4, 4))
    
    # before update, all zero
    assert df1.loc[0, 0] == approx(0)
    
    # after update
    df1.update(df2)
    assert df1.loc[0, 0] != 0


if __name__ == "__main__":
    #
    test_update()


def test_filter_func():
    """
    
    **中文文档**
    
    fiter_func可以做到只对符合条件的元素update。
    """
    df1 = pd.DataFrame(np.zeros((4, 4)))
    df2 = pd.DataFrame(np.random.randn(4, 4))
    
    # 将所有小于0的元素用全0矩阵中的0替换
    df2.update(df1, filter_func=lambda x: x < 0)
    for column in df2:
        for value in df2[column]:
            assert value >= 0
    

if __name__ == "__main__":
    #
    test_filter_func()

