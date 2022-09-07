"""
计算两个日期之间相隔的天数
"""
import datetime

time1 = datetime.datetime.strptime('2022-08-12 12:00:32', '%Y-%m-%d %H:%M:%S')
time2 = datetime.datetime.strptime('2022-08-18 12:00:32', '%Y-%m-%d %H:%M:%S')
print((time2 - time1).days)
