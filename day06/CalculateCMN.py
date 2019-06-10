"""
输入M和N计算C(M,N)
Author: zhouju
Version: 0.1
Date: 2019-06-10
"""
import math

M = int(input("M = "))
N = int(input("N = "))
fm = 1
for i in range(1, M + 1):
    fm *= i
fn = 1
for i in range(1, N + 1):
    fn *= i
fmn = 1
for i in range(1, M - N + 1):
    fmn *= i

print(fm / (fn * fmn))


def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac


print(factorial(M) / (factorial(N) * factorial(M - N)))

print(math.factorial(M) / (math.factorial(N) * math.factorial(M - N)))
