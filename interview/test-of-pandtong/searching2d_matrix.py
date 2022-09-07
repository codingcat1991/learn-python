def search_matrix(matrix, target):
    a = []
    for i in matrix:
        a.extend(i)
    return target in a


matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
print(search_matrix(matrix, 3))
print(search_matrix(matrix, 8))
