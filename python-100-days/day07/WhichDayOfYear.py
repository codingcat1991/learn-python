"""
计算指定的年月日是这一年的第几天
Author: zhouju
Version: 0.1
Date: 2019-06-11
"""


def is_leap_year(year):
    """
    判断指定年份是不是闰年
    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def which_day(year, month, day):
    """
    计算传入的日期是这一年的第几天
    :param year:年
    :param month:月
    :param day:日
    :return:第几天
    """
    day_of_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += day_of_month[index]
    total += day
    return total


if __name__ == '__main__':
    print(which_day(2019, 6, 11))
