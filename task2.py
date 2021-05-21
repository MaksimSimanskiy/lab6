#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    c = int(input("Введите начало интервала "))
    d = int(input("Введите конец интервала "))
    a = []
    k = 0;
    for i in range(5):
        a.append(float(input(f'Введите элемент списка {i} - ')))

    print('Максимальный элемент ' , max(a, key=abs))
    print('Индекс максимального элемента ' , a.index(max(a, key=abs)))

    k =(list(filter(lambda i: i > 0, a))[0])
    k = a.index(k)
    print('Сумма чисел после первого положительного числа',sum(a[k:]))
    print('Отсортированый массив',sorted(a,key = lambda x: d > x > c,reverse = True))
