"""
计算n的阶乘
"""

def factorial(n):
    """递归实现"""
    if n < 0:
        raise ValueError
    if n == 1:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


def factorial1(n):
    """非递归实现"""
    if n < 0:
        raise ValueError
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac


print(factorial1(4))
