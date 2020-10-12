# 冒泡排序
def bubble_sort(l):
    for i in range(1, len(l)):
        for j in range(0, len(l) - 1):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
    return l


# 合并排序

# 插入排序
def insertion_sort(l):
    for i in range(len(l)):
        pre_index = i - 1
        current = l[i]
        while pre_index >= 0 and l[pre_index] > current:
            l[pre_index + 1] = l[pre_index]
            pre_index -= 1
        l[pre_index + 1] = current
    return l


# 希尔排序

# 选择排序
def selection_sort(l):
    for i in range(0, len(l) - 1):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[min_index] > l[j]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return l
