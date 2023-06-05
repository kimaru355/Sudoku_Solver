#!/usr/bin/python3

import copy

a = [[3, 5, 6],
     [7, 8, 9]]

b = a.copy()
c = a[:]
d = copy.copy(a)
e = copy.deepcopy(a)
print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = 0
print(a)
print(b)
print(c)
print(d)
print(e)
