"""
将一个数组逆序输出
"""
li = [1, 7, 4, 7, 4, 2, 5]
print(li[::-1])
new_li = []
for i in range(len(li), 0, -1):
    new_li.append(li[i - 1])
print(new_li)
for i in range(len(li) // 2):
    li[i], li[-i - 1] = li[-i - 1], li[i]
print(li)
li.reverse()
print(li)
