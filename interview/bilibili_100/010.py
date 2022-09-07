"""
第010集 怎样对简单列表元素排序
怎样对简单列表排序？
简单列表：元素类型不是复合类型（列表/元组/字典）
形式1:[20, 50, 10, 40, 30]
•形式2：[bb’，"ee’，"aa,'dd,'cc']
知识点：
怎样原地排序？怎样不改变原列表排序？
怎样指定是升序还是隆序排序？
"""


def sort_list(li: list):
    return sorted(li, key=lambda x: x, reverse=False)


print(sort_list([20, 50, 10, 40, 30]))
