import random

list1 = []
for item in range(1, 10):
    list1.append(random.randrange(1, 10, 1))
print(list1)

list2 = [i for i in range(1, 10) ]
print(list2)