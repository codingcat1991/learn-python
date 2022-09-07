"""
打印杨辉三角
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1  6   15 20 15 6 1
1  7  21  35  35 21 7 1
1 8  28 56  70  56 28 8 1
1 9 36 84 126 126 84 36 9 1
"""
n = 10
li = []
for i in range(n):
    li.append([])
    for j in range(i + 1):
        if j == 0 or j == i:
            li[i].append(1)
        else:
            li[i].append(li[i - 1][j - 1] + li[i - 1][j])
for i in li:
    print(i)
