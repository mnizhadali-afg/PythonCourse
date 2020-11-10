numbers = list(range(1, 16))

print(numbers)

# Select number's even integers
numbers[1:len(numbers):2]

# Replace the elements at indices 5 through 9 with 0s,
numbers[5:10] = [0] * len(numbers[5:10])
numbers

# Keep only the first five elements
numbers[5:] = []
numbers


# Delete all the contents from the list
numbers[:] = []