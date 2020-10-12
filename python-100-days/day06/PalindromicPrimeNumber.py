"""
判断输入的正整数是不是回文素数
Author: zhouju
Version: 0.1
Date: 2019-06-10
"""

from PrimeNumber import is_prime
from PalindromicNumber import is_palindromic_2


def is_palindromic_prime(num):
    return is_prime(num) and is_palindromic_2(num)


if __name__ == "__main__":
    x = int(input("请输入一个正整数："))
    print(is_palindromic_prime(x))
