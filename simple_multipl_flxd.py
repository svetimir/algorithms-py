# -*- coding: utf-8 -*-

# AUTHOR: Georgy Yashin, ifi@yandex.ru
# DATE: 28.08.2017
# DESCRIPTION: нахождение простых множителей числа

import math

def find_factors_flxd(n):
    factors=list()
    #проверяем делимость на 2
    while n%2==0:
        factors.append(2)
        n=n/2
    #ищем нечетные множители
    i=3
    max_fact=math.sqrt(n)
    while i<=max_fact:
        while n%i==0:
            factors.append(i)
            n=n/i
            max_fact=math.sqrt(n)
        i+=2
    if n>1: factors.append(n)
    return factors

print(find_factors_flxd(531441))
