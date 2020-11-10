f = [41, 32, 212]

v = list(map(lambda x: (x - 32) * 5 / 9, f))
print(v)

rev = [item ** 2 for item in reversed(f)]
print(rev)