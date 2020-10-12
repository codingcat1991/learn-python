from array import *

array1 = array('i', [10, 20, 30, 40, 50])
for x in array1:
    print(x)

# 访问数组元素
print(array1[0])

# 插入操作
array1.insert(1, 60)
for x in array1:
    print(x)

# 删除
array1.remove(60)
for x in array1:
    print(x)

# 查找/搜索
print(array1.index(50))

# 更新
array1[2] = 1000
print(array1[2])
for x in array1:
    print(x)

# ===== 二维数组  =====
T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
print(T[0])
print(T[1][2])
# 在二维数组中插入值
T.insert(2, [0, 5, 11, 13, 6])
for r in T:
    for c in r:
        print(c, end=" ")
    print()

# 更新二维数组中的值
T[2] = [11, 9]
T[0][3] = 7
for r in T:
    for c in r:
        print(c, end=" ")
    print()
# 删除二维数组中的值
del T[3]
for r in T:
    for c in r:
        print(c, end=" ")
    print()
