"""第004集 区间内的所有素效
输入开始数字和结束数字，打印区间内所有的素数
比如：输入11和25，打印11~25的所有素数，包括25
素数：如果数字只能被1和自己整除就是素数，否则不是素数
比如3是素数、4不是素数"""


def is_prime(n):
    if n <= 0:
        return False
    if n <= 3:
        return True
    for i in range(1, n // 2 + 1):
        if n % i == 0 and i != 1:
            return False
    return True


def prime_number(start, end):
    prime_list = []
    for i in range(start, end):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


print(prime_number(1, 10))
