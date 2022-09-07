"""
计算日期数据周同比
旧期 销售额
2021-04-16 93
2021-04-17 88
2021-04-18 91
2021-04-19 84
2021-04-20 88
2021-04-21 99
2021-04-22 85
2021-04-23 73
2021-04-24 75
2021-04-25 95
2021-04-26 90
2021-04-27 72
2021-04-28 75
2021-04-29 84
2021-04-30 90
2021-05-01 93
2021-05-02 64
2021-05-03 85
2021-05-04 86
2021-05-05 60
2021-05-06 83
"""
import datetime

with open('sale', 'r') as f:
    content = f.read()
data = {}
for row in content.split('\n'):
    row = row.split(' ')
    data[row[0]] = int(row[1])
delta = datetime.timedelta(days=7)


def str2date(s):
    return datetime.datetime.strptime(s, '%Y-%m-%d')


def date2str(d: datetime.datetime):
    return d.strftime('%Y-%m-%d')


huanbi = {}
for d, s in data.items():
    cur_date = str2date(d)
    pre7date = date2str(cur_date - delta)
    if not pre7date in data:
        huanbi[pre7date] = 0
        continue
    huanbi[pre7date] = (data[d] - data[pre7date]) / data[pre7date]

print(huanbi)
