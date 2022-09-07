"""
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
原始列表：[1,4,6,9,13,16,19,28,40,100]
插入数字：7
结果列表：[1,4,6,7,9,13,16,19,28,40,100]
"""

source = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]
insert = 7

if insert < source[0]:
    source = [insert] + source
if insert > source[-1]:
    source.append(insert)

for idx, ele in enumerate(source):
    if ele < insert < source[idx + 1]:
        source = source[0:idx + 1] + [insert] + source[idx + 1:]
        break

print(source)
