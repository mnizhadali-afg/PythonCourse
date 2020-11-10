a = [[77, 68, 86], [96, 87, 89], [70, 90, 86]]

for row in a:
    for col in row:
        print(col, end=' ')
    print()

print('\n\n')

for i, row in enumerate(a):
    for j, col in enumerate(row):
        print(f'a[{i}][{j}]={col}', end='  ')
    print()