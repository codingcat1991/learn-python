"""
第009集 怎样对列表元素去重
输入，包含重复元素的原始列表：
[10, 20, 30, 10, 20]
•返回：
[10, 20, 30]
"""


def distinct_list(li):
    # return list(set(li))
    rst = []
    for i in li:
        if i not in rst:
            rst.append(i)
    return rst


print(distinct_list([1, 2, 3, 2, 5]))
