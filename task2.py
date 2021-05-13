#!/usr/bin/env python3
# -*- coding: utf-8 -*-
c = int(input("Введите начало интервала "))
d = int(input("Введите конец интервала "))
a = []

for i in range(5):
    a.append(float(input(f'Введите элемент списка {i} - ')))

print('Максимальный элемент ' , max(a, key=abs))
print('Индекс максимального элемента ' , a.index(max(a, key=abs)))
for i in a:
    if (a[i] > 0.):
        k = i
        break
print('Сумма чисел после первого положительного числа',sum(a[k:]))
print('Отсортированый массив',sorted(a,key = lambda x: d > x > c,reverse = True))
