nums = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

def isOdd(x):
    """Returns True only if the x is odd."""
    return x % 2 != 0

v = list(filter(isOdd, nums))
v2 = list(filter(lambda x: x % 2 != 0, nums))

print(v)
print(v2)