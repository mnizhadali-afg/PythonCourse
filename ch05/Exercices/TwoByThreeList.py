t = [[10, 7, 3], [20, 4, 17]]

total = 0
items = 0

for row in t:
    for item in row:
        total += item
        items += 1
print(total / items)

total = 0
items = 0

for row in t:
    total += sum(row)
    items += len(row)
print(total / items)
