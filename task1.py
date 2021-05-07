#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = []
b = []
for i in range(10):
    a.append(int(input("Введите элемент списка " + str(i) + ' - ')))
    b = list(filter(lambda x: 20 > x > 2 and x % 8 == 0, a))
print('Список А = {}\nВыбраные элементы = {} \nКоличество элементов  = {} \nСумма = {}'.format(a, b, len(b), sum(b)))