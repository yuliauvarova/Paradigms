def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[i] < numbers[j]:
                temp = numbers[j]
                numbers[j] = numbers[i]
                numbers[i] = temp
    return numbers


numbers = [63, 3, 0, 13, -45, -8, 4, 23, 43, 1, -23]
print(numbers)
# sort_list_imperative(numbers)
# print(numbers)


def sort_list_declarative(numbers):
    list.sort(numbers)

sort_list_declarative(numbers)
print(numbers)