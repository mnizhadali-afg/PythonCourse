colors = ['red', 'yellow', 'blue']

listEnum = list(enumerate(colors))
tupleEnum = tuple(enumerate(colors))

print('list: ', listEnum)
print('tuple: ', tupleEnum)
print()

for index, value in enumerate(colors):
    print(f'{index}: {value}')