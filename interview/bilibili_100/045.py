"""
统计 1 到 100 之和。
"""
s = 0
for num in range(1, 101):
    s += num
print(s)

print(sum([num for num in range(1, 101)]))
