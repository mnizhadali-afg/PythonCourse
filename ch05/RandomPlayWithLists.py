import random
list1 = []

for item  in range(1, 10):
    list1.append(random.randrange(1, 100, 1))

print('List created: ', list1)

for i in range(len(list1)):
    if (list1.pop() == random.randrange(1, 100, 1)):
        break

if (len(list1) == 0):
    print('Vanished List')
else:
    print(len(list1), " values are remained in the list, which are: ", list1)