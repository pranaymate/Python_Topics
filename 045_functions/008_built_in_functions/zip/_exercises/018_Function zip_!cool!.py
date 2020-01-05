a = [1, 20, 30, 40]           # list
b = ['a', 'b', 'c', 'd', 'e']   # list
for i, j in zip(a, b):
    print(i, j)

# 10 a
# 20 b
# 30 c
# 40 d

for i in zip(a, b):
    print(i, type(i))

# (10, 'a') <class 'tuple'>
# (20, 'b') <class 'tuple'>
# (30, 'c') <class 'tuple'>
# (40, 'd') <class 'tuple'>

import itertools
a = [10, 20, 30, 40]              # list
b = ['a', 'b', 'c', 'd', 'e']      # list
c = [1.1, 1.2]                  # list
for i in itertools.zip_longest(a, b, c):
    print(i)

# (10, 'a', 1.1)
# (20, 'b', 1.2)
# (30, 'c', None)
# (40, 'd', None)
# (None, 'e', None)
print()
for i in itertools.zip_longest(a, b, c, fillvalue=0):
    print(i)

# (10, 'a', 1.1)
# (20, 'b', 1.2)
# (30, 'c', 0)
# (40, 'd', 0)
# (0, 'e', 0)

a = [10, 20, 30, 40]         # list
c = [1.1, 1.2, 1.3, 1.4]     # list
ac = zip(a, c)
print(type(ac))
# <class 'zip'>
ac = list(ac)
print(type(ac))
# <class 'list'>
print(ac)
# [(10, 1.1), (20, 1.2), (30, 1.3), (40, 1.4)]

values = [1.34, 3.25, 2.99]     # list
coefficient = [3, 2, 2]         # list
for i, j in zip(values, coefficient):
    print(i * j)

# 4.0200000000000005
# 6.5
# 5.98

a = []                        # list
b = []                        # list
for i, j in zip(range(10, 20), range(1, 10)):
    a.append(i)

b.append(j)

print(a)
# [10, 11, 12, 13, 14, 15, 16, 17, 18]
print(b)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
