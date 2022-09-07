"""
第008集 移除列表中的多个元素
输入：
原始列表：[3, 5, 7, 9, 11, 13]
•移除元素：[7,11]
返回：
[3, 5, 9, 13]
"""


def remove_element(source, delete):
    # return list(set(source) - set(delete))
    for i in delete:
        source.remove(i)
    return source


print(remove_element([3, 5, 7, 9, 11, 13], [7, 11]))
