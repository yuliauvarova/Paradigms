def normalize(lst):
    min_val = min(lst)
    max_val = max(lst)
    normalized = list(map(lambda x: (x - min_val) / (max_val - min_val), lst))
    return normalized


lst = (1, 3, 4, 6, 2, 7, 35)

lst1 = normalize(lst)

for x in range(len(lst1)):
    print(lst1[x])
