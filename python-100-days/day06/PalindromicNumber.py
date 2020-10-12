"""
判断一个数是不是回文数的函数
Author: zhouju
Version: 0.1
Date: 2019-06-10
"""


def is_palindromic_1(x):
    s_str = str(x)
    reverse_str = s_str[::-1]
    return x == int(reverse_str)


def is_palindromic_2(x):
    temp = x
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp = temp // 10
    return x == total


if __name__ == "__main__":
    num = int(input("请输入数字："))
    print(is_palindromic_1(num))
    print(is_palindromic_2(num))
