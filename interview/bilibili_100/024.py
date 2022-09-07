"""
计算人意7天前的日期
"""
import datetime

time = datetime.datetime.strptime('2022-08-12 12:00:32', '%Y-%m-%d %H:%M:%S')
time_7 = time - datetime.timedelta(days=7)
print(time_7)
