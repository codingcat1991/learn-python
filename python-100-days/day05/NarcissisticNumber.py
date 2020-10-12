"""
寻找“水仙花数”
Author: zhouju
Version: 0.1
Date: 2019-06-10
"""


def narcissistic_number_1():
    num = int(input("请输入一个正数："))
    num_str = str(num)
    length = len(num_str)
    num_sum = 0
    for i in range(length):
        num_sum += int(num_str[i:i + 1]) ** length
    if num_sum == num:
        print("%d是%d位的水仙花数" % (num, length))
    else:
        print("%d不是水仙花数" % num)


def narcissistic_number_2():
    num = int(input("请输入一个正数："))
    length = len(str(num))
    num_sum = 0
    for i in range(length):
        num_sum += (int(num // (10 ** i)) % 10) ** length
    if num_sum == num:
        print("%d是%d位的水仙花数" % (num, length))
    else:
        print("%d不是水仙花数" % num)


narcissistic_number_2()
narcissistic_number_1()
