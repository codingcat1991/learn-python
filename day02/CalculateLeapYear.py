"""
输入年份判断是否闰年
Author: zhouju
Version: 0.1
"""
year = int(input('请输入年份：'))
isLeapYear = '不是'
if year % 4 == 0 and year % 100 != 0:
    isLeapYear = '是'
if year % 100 == 0 and year % 400:
    isLeapYear = '是'

print("%d年%s闰年" % (year, isLeapYear))
