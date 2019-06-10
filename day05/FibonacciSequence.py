"""
生成“斐波拉切数列”
Author: zhouju
Version: 0.1
Date: 2019-06-10
"""


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("请输入一个正整数："))
for i in range(1, num + 1):
    print(fibonacci(i), end=' ')
