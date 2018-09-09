# -*- coding: utf-8 -*-

# Упражнения из книги
# "Алгоритмы. Теория и практическое применение", Род Стивенс

# AUTHOR: Georgy Yashin, ifi@yandex.ru
# DATE: 27.08.2017
# LATEST REVISION: 08.09.2018

import math
import random

def f(x):
    pass;

# наибольший общий делитель
def gcd(a,b):
    while b>0.01:
        r=math.fmod(a,b)
        a=b
        b=r
    return a

# проверка на дубликаты
def dub(a):
    j=0
    d=0
    for i in range(0,len(a)):
        for j in range(j+i,len(a)):
            if(a[i]==a[j]):
                d+=1
        j=0
    return d

# рандомизация массива
# генерация массивов со случайными числами
def create_array(size): return [random.randint(0,10) for i in range(0,size)]

def randomize_array(a):
    for i in range(len(a)):
        j=random.randint(i,len(a)-1)
        tmp=a[i]
        a[i]=a[j]
        a[j]=tmp
    return a

if __name__=="__main__":
    print("testing "+gcd.__name__)
    print(gcd(531441, 120000))
    print("testing "+create_array.__name__)
    a = create_array(5)
    print(a)
    print("testing "+dub.__name__)
    print(dub(a))
    print("testing "+create_array.__name__)
    a, b = create_array(10), create_array(10)
    print(a, b)
    print("testing "+randomize_array.__name__)
    print(randomize_array(a),randomize_array(b))
