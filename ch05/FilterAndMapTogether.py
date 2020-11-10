nums = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

v = list(map(lambda x: x** 2, filter(lambda x: x % 2 != 0, nums)))
print(v)