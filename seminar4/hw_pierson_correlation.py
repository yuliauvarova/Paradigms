import math

arr1 = (1, 2, 3, 4, 5, 4, 3, 2, 1, 1)
arr2 = (100, 200, 300, 400, 500, 400, 300, 200, 100, 100)


def calc_ar_mean(arr):
    mean = sum(arr) / len(arr)
    return mean


def pierson_cor(arr1, arr2):
    mean_arr1 = calc_ar_mean(arr1)
    mean_arr2 = calc_ar_mean(arr2)
    list_elem_arr1_minus_mean = list(map(lambda x: x - mean_arr1, arr1))
    list_elem_arr2_minus_mean = list(map(lambda x: x - mean_arr2, arr2))
    stage1 = sum(list(map(lambda x, y: x * y, list_elem_arr1_minus_mean, list_elem_arr2_minus_mean)))
    stage2 = math.sqrt(sum(list(map(lambda x, y: x ** 2 * y ** 2, list_elem_arr1_minus_mean, list_elem_arr2_minus_mean))))
    return stage1 / stage2


print(pierson_cor(arr1,arr2))
