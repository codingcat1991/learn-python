"""
判断一个数是不是素数的函数
Author: zhouju
Version: 0.1
Date: 2019-06-10
"""


def is_prime(num):
    for i in range(2, int(num // 2)):
        if num % i == 0:
            return False
    return True if num != 1 else False


if __name__ == "__main__":
    x = int(input("请输入一个正整数："))
    print(is_prime(x))
