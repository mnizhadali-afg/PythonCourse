def calculate_product(*args):
    pr = 1
    for value in args:
        pr *= value
    return pr

print("\nProduct is: ", calculate_product(43, 12, 11, 10, 9))