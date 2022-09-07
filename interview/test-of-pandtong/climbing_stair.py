def climb_stair(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


def climb_stair_crazy(n):
    if n == 0:
        return 1
    return 2 ** (n - 1)


print(climb_stair_crazy(0))  # 1
print(climb_stair_crazy(1))  # 1
print(climb_stair_crazy(2))  # 2
print(climb_stair_crazy(3))  # 4
print(climb_stair_crazy(4))  # 8
print(climb_stair_crazy(5))  # 16
print(climb_stair_crazy(6))  # 32
