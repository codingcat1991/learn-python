"""
计算日期范围内的所有日期
"""
import datetime


def get_range_date(start, end):
    dates = []
    delta = datetime.timedelta(days=1)
    while start <= end:
        dates.append(start)
        start = start + delta
    return dates


start_time = datetime.datetime.strptime('2022-08-12 12:00:32', '%Y-%m-%d %H:%M:%S')
end_time = datetime.datetime.strptime('2022-08-18 12:00:32', '%Y-%m-%d %H:%M:%S')

print(get_range_date(start_time, end_time))
