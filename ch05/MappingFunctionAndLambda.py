nums = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

def squares(x):
    """Squares the values in the list"""
    return x ** 2

v2 = list(map(squares, nums))
v = list(map(lambda x: x ** 2, nums))
v3 = list(item ** 3 for item in nums)

print("Higher Order Function: \t", v2)
print("Lambda: \t\t\t\t", v)
print("V3: \t\t\t\t\t", v3)