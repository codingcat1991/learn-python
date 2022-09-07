"""
将unix时间错转换成日期
"""
import datetime


def timestamp2datetime(n: int):
    return datetime.datetime.fromtimestamp(n)


print(timestamp2datetime(111))
