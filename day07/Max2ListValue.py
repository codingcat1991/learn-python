"""
设计一个函数返回传入的列表中最大和第二大的元素的值。
Author: zhouju
Version: 0.1
Date: 2019-06-11
"""


def get_max_second_max_value(l):
    """
    获取列表中最大和第二大的元素的值
    :param l:传入的列表
    :return:最大和第二大值组成的元组
    """
    if len(l) < 2:
        return tuple(l)
    l.sort(reverse=True)
    return l[0], l[1]


def max2(l):
    """
    获取列表中最大和第二大的元素的值
    :param l: 传入的列表
    :return: 最大和第二大值组成的元组
    """
    if len(l) < 2:
        return tuple(l)
    m1, m2 = (l[0], l[1]) if l[0] > l[1] else (l[1], l[0])
    for index in range(2, len(l)):
        if l[index] > m1:
            m2 = m1
            m1 = l[index]
        elif l[index] > m2:
            m2 = l[index]
    return m1, m2


if __name__ == '__main__':
    print(max2([1, 4, 2, 6, 6, 3]))

# 疑问：列表只有一个元素以及列表数据重复是否需要处理？
