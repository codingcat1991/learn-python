"""
寻找“完美数”
Author: zhouju
Version: 0.1
Date: 2019-06-10
"""
num = int(input("请输入一个正整数："))
num_sum = 0
for i in range(1, int(num // 2) + 1):
    if num % i == 0:
        num_sum += i
if num_sum == num:
    print("%d是完美数" % num)
else:
    print("%d不是完美数" % num)
