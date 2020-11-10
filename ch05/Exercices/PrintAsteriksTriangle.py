"""The program print the Aesterieks traingle"""
n = 10

for i in range(n):
    for j in range(i):
        print('*', end=' ')
    print('*')

for i in range(n):
    for j in range(i):
        print((' ' * j - 1), '*')
    print('*')