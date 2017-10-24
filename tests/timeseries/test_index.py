#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytz
from dateutil.tz import tzstr
import pandas as pd
from datetime import datetime


def get_utcoffset_in_seconds(tz):
    return tz.utcoffset(datetime.utcnow()).total_seconds()


utc = pytz.utc
utc8 = tzstr("UTC+08:00")
epoch = datetime.utcfromtimestamp(0).replace(tzinfo=utc)

assert get_utcoffset_in_seconds(utc) == 0
assert get_utcoffset_in_seconds(utc8) == 3600 * 8

# 对于时间序列而言，两个Index即使使用的是不同的时区，只要绝对时间相同，就会被视为
# 相同的时间，从而能成功地join。
df1 = pd.DataFrame(
    {"v1": [1, 1]},
    index=[
        datetime(2000, 1, 10, tzinfo=utc),
        datetime(2000, 1, 11, tzinfo=utc),
    ]
)

df2 = pd.DataFrame(
    {"v2": [2, 2]},
    index=[
        datetime(2000, 1, 11, 8, tzinfo=utc8),
        datetime(2000, 1, 12, 8, tzinfo=utc8),
    ]
)

df = df1.join(df2, how="outer")
assert len(df.index) == 3