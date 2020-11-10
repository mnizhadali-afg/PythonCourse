nums = list(range(1, 16))

vFilter = list(filter(lambda x: x % 2 == 0, nums))
vMap = list(map(lambda x: x ** 2, nums))
vFilterMap = list(map(lambda x: x **2, filter(lambda x: x % 2 == 0, nums)))

print("Initial list: \t", list(nums))
print("Filter (Evens): ",vFilter)
print("Map (Squares): \t",vMap)
print("Filter and Map: ", vFilterMap)