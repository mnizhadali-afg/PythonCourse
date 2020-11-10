"""Displaying a Bar Chart using enumerate"""
numbers = [19, 11, 7, 21, 10]

print('\nCreating a Bar Chart from numbers')
print(f'Index{"Value":>8}     Bar')

for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8}     {"*" * value}')