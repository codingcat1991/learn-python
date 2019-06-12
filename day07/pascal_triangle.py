"""
打印杨辉三角
Author: zhouju
Version: 0.1
Date: 2019-06-11
"""


def pascal_triangle(num):
    """
    打印杨辉三角形
    :param num: 三角形行数
    :return: 无返回值
    """
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    pascal_triangle(10)
