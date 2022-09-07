"""
第005集 求前N个数字的平万和

输入：数字N
•计算：12+22+32+.+
"""


def cal_squire_sum(n):
    s = 0
    for i in range(1, n + 1):
        s += i * i
    return s


print(cal_squire_sum(2))
