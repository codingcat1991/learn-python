"""
函数不确定参数个数
Author: zhouju
Version: 0.1
Date: 2019-06-10
"""


def add(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
