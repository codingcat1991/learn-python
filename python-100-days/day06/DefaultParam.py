"""
函数默认参数
Author: zhouju
Version: 0.1
Date: 2019-06-10
"""


def add(a=0, b=0, c=0):
    return a + b + c


print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
