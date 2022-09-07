"""
计算数字范围中的偶数
"""


def get_odd_num(start, end):
    return [i for i in range(start, end + 1) if i % 2 == 0]
    # odds = []
    # for i in range(start, end + 1):
    #     if i % 2 == 0:
    #         odds.append(i)
    # return odds


print(get_odd_num(1, 10))
