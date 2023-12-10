src_arr = [1, 5, 12, 67, 9, 12, 3]


def bubble_sort(arr):
    for j in range(len(arr) - 1):
        for i in range(len(arr) - j - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
    return arr


def binary_search(arr, elem, delta=0):
    i = int(len(arr) / 2)
    if elem == arr[i]:
        return i + delta
    elif len(arr) == 1:
        return -1
    elif elem < arr[i]:
        return binary_search(arr[:i], elem, delta + 0)
    elif elem > arr[i]:
        return binary_search(arr[i:], elem, delta + i)


def search(arr, elem):
    arr = bubble_sort(arr)
    return binary_search(arr, elem)


print(search(src_arr, 5))
