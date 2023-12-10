arr = [1, 2, 3, 4, 1, 2, 9, 3]

# реализация с выведениемвсех дубликатов по одному разу
def get_counts(arr):
    result = {}
    for item in arr:
        result[item] = result.get(item, 0) + 1
    return result


def find_duplicates(arr):
    unique_elements = set(arr)
    counts = get_counts(arr)
    return list(filter(lambda elem: counts[elem] > 1, unique_elements))

print(find_duplicates(arr))

# реализация с выведением всех дубликатов, которые встречаются 2 раза и чаще

def get_dub(arr):
    buffer = set()
    res_list = []
    for i in arr:
        if i in buffer:
            res_list.append(i)
        else:
            buffer.add(i)
    return res_list

print(get_dub(arr))