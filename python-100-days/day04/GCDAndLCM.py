"""
输入两个正整数计算最大公约数和最小公倍数

Author: zhouju
Version: 0.1
Date: 2019-06-09
"""

a = int(input("a = "))
b = int(input("b = "))
gcd = min(a, b)
lcm = max(a, b)
for i in range(gcd, 0, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        break
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1
print("最大公约数：%d" % gcd)
print("最小公倍数：%d" % lcm)

if a > b:
    a, b = b, a
for factor in range(a, 0, -1):
    if a % factor == 0 and b % factor == 0:
        print("%d和%d的最大公约数为%d" % (a, b, factor))
        print("%d和%d的最小公倍数为%d" % (a, b, a * b // factor))
        break
