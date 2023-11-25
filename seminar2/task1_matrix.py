import math

matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def matrix_trace(array):
    n = int(math.sqrt(len(array)))
    diag_sum = array[0]
    i = 0
    while i < len(array) - n - 1:
        i = i + n + 1
        diag_sum = diag_sum + array[i]
    return diag_sum


print(matrix_trace(matrix))
