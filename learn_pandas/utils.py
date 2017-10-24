#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def assert_value_equal(df_or_ndarray, values):
    try:
        condition = (df_or_ndarray.values == values).all()
    except AttributeError:
        condition = (df_or_ndarray == values).all()
    assert condition


class Timer(object):
    def __init__(self):
        self.elapse = None

    def __enter__(self):
        self._now = time.clock()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        now = time.clock()
        self.elapse = now - self._now
        self._now = now
