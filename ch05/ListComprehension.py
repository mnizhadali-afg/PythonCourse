import random

list1 = []
for i in range(1, 8):
    list1.append(random.randrange(1, 100))
print(list1)

list2 = [i ** 2 for i in range(1, 10)]
print(list2)