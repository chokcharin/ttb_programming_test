
list_a = [1, 2, 3, 5, 6, 8, 9]
list_b = [3, 2, 1, 5, 6, 0]
duplicate = list()

for item in list_a:
    if item in list_b:
        duplicate.append(item)

print(duplicate)