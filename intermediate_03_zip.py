#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

x = [1, 2, 3, 4]
y = [6, 7, 8, 9]
z = ['a', 'b', 'c', 'd']

for a, b in zip(x,y):
    print(a, b)
print('-'*60)

for a, b, c in zip(x,y,z):
    print(a, b, c)
print('-'*60)

# zip类型
print(type(zip(x,y,z)))
print('-'*60)

# zip转换为list
print(list(zip(x,y,z)))
print('-'*60)

Names = ['Jill','Jack','Jeb','Jessica']
Grades = [99,56,24,87]
print('-'*60)

# zip转换为dic
d = dict(zip(Names, Grades))
print(d)
print('-'*60)

[print(a, b, c) for a, b, c in zip(x, y, z)]
print('-'*60)

x = [1, 2, 3, 4]
y = [6, 7, 8, 9]
z = ['a', 'b', 'c', 'd']
[print(x, y, z) for x, y, z in zip(x, y, z)]
print(x)

x = [1, 2, 3, 4]
y = [6, 7, 8, 9]
z = ['a', 'b', 'c', 'd']
for x, y, z in zip(x, y, z):
    print(x, y, z)

# for循环后，x，y, z的值均为最后一次循环所得值，所以后续打印x, y, z不再是list
print(x, y, z)
