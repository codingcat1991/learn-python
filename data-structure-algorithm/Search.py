# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 16:58
# @Author  : JacobZhou
# @Email   : JacobZhou@canway.net
# @File    : Search.py
# @Project : AlgorithmInterview


def linear_search(values, search_for):
    search_at = 0
    search_res = False
    while search_at < len(values) and not search_res:
        if values[search_at] == search_for:
            search_res = True
        else:
            search_at += 1
    return search_res



def intpolsearch(values, x):
    # idx0 = 0
    # idxn = len(values) - 1
    # while idx0 <= idxn and x >= values[idx0] and x <= values[idxn]:
    #     mid = math.ceil((idx0 + idxn) / 2)
    #     if values[mid] == x:
    #         return "Found " + str(x) + " at index " + str(mid)
    #     elif values[mid] < x:
    #         idx0 = mid + 1
    #     else:
    #         idxn = mid - 1
    # return "Searched element not in the list"
    idx0 = 0
    idxn = (len(values) - 1)

    while idx0 <= idxn and x >= values[idx0] and x <= values[idxn]:

        # Find the mid point
        mid = idx0 + \
              int(((float(idxn - idx0) / (values[idxn] - values[idx0]))
                   * (x - values[idx0])))

        # Compare the value at mid point with search value
        if values[mid] == x:
            return "Found " + str(x) + " at index " + str(mid)

        if values[mid] < x:
            idx0 = mid + 1
    return "Searched element not in the list"


l = [2, 6, 11, 19, 27, 31, 45, 121]
print(intpolsearch(l, 2))
