"""
函数计算最大公约数喝最小公倍数
Author: zhouju
Version: 0.1
Date: 2019-06-10
"""


def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def lcm(x, y):
    return x * y // gcd(x, y)


if __name__ == "__main__":
    a = int(input("x = "))
    b = int(input("y = "))
    print("最大公约数：%d" % gcd(a, b))
    print("最小公倍数：%d" % lcm(a, b))
