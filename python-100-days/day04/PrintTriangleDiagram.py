"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Author: zhouju
Version: 0.1
Date: 2019-06-09
"""
row = int(input("请输入行数："))

for i in range(row):
    for j in range(i + 1):
        print("*", end="")
    print()

for i in range(row):
    for k in range(i, row - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print()

for i in range(row):
    for k in range(i, row - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    for n in range(row, row + i):
        print("*", end="")
    print()

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
