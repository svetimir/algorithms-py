# -*- coding: utf-8 -*-

# решето Эратосфена

# AUTHOR: Georgy Yashin, ifi@yandex.ru
# DATE: 29.08.2017
# LATEST REVISION: 08.09.2018

def eratosthenes_flxd(max_num):
    """
        Функция ищет все простые числа
        в интервале от 0 до max_num
        и возвращает массив таких чисел
    """
    table=[True for i in range(max_num+1)]
    t=2
    while t<max_num:
        for i in range(2*t,max_num+1,t):
            table[i]=False
        t+=1
        while not table[t] and t<max_num:
            t+=1
    s=[]
    j=0
    for i in table:
        if i:
           s.append(j)
        j+=1
    return s

if __name__=="__main__":
    print("testing "+eratosthenes_flxd.__name__)
    print("Prime numbers found:\n",eratosthenes_flxd(1000))

