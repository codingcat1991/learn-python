from numpy import *

a = array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
           ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
           ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
           ['Sun', 13, 15, 19, 16]])

m = reshape(a, (7, 5))
print(m)

# 访问矩阵中的值
print(m[2])
print(m[2][0])

# 添加一行
m_r = append(m, [['Avg', 12, 15, 13, 11]], 0)
print(m_r)

# 添加一列
m_c = insert(m, [5], [[1], [2], [3], [4], [5], [6], [7]], 1)
print(m_c)

# 从矩阵中删除一行
m_d_r = delete(m, [2], 0)
print(m_d_r)

# 从矩阵中删除一列
m_d_c = delete(m, [2], 1)
print(m_d_c)

# 更新矩阵中的一行
m[3] = ['Thu', 0, 0, 0, 0]
print(m)
