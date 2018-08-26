#!/usr/bin/python
# -*- coding: utf-8 -*-

# こうやってもできる
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

# こうやってもできる
number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)

# こうやってもできる
number_list = list(range(1, 6))
print(number_list)

# リスト内包表記を使うとこう
# [expression for item in iterable]
number_list = [number for number in range(1, 6)]
print(number_list)

# 条件式も追加できる
# [expression for item in iterable if condition]
odd_list = [number for number in range(1, 6) if number % 2 == 1]
print(odd_list)

# for節も使える
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

# 包括表記を使うとこう
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)
    
