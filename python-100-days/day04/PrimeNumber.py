"""
输入一个正整数判断它是不是素数

Author: zhouju
Version: 0.1
Date: 2019-06-09
"""
import math

num = int(input("请输入一个正整数："))
is_prime = True
for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime is True:
    print("%d是素数！" % num)
else:
    print("%d不是素数！" % num)
