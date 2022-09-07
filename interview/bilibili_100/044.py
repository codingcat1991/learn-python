"""
两个矩阵相加。
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
"""


def sum_matrix(x, y):
    # s = []
    # for i in range(len(x)):
    #     for j in range(len(y)):
    #         if not i == j:
    #             continue
    #         tmp = []
    #         for m in range(len(x[i])):
    #             for n in range(len(y[j])):
    #                 if not m == n:
    #                     continue
    #                 tmp.append(x[i][m] + y[j][n])
    #         s.append(tmp)
    # return s
    rst = [[0 for _ in range(len(x[0]))] for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            rst[i][j] = x[i][j] + y[i][j]
    return rst


X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]
rst = sum_matrix(X, Y)
print(rst)
