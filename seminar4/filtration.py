# def get_count(people, min_age):
#     count = 0
#     for key_person, key_value in people.items:
#         if key_value < min_age:
#             count += 1
#     return count


people = {"Sergey": 20, "Maxim": 32, "Alex": 26}

# print(get_count(people, 30))

min_age = 30

def filter_min_age(dict, min_age):
    return sum(map(lambda name: dict[name] < min_age, dict))

print(filter_min_age(people, min_age))
