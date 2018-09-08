# -*- coding: utf-8 -*-

# нахождение наибольшего общего делителя
# алгоритм Евклида

# AUTHOR: Georgy Yashin, ifi@yandex.ru
# DATE: 28.08.2017
# LATEST REVISION: 08.09.2018

import math

def euq_flxd(a,b):
    r=0
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

if __name__=="__main__":
    a=[4851,3003,531441,24]
    print("testing "+euq_flxd.__name__+" with values: ")
    print("{} {}\n{} {}".format(a[0],a[1],a[2],a[3]))
    print("got:")
    print(euq_flxd(a[0],a[1]))
    print(euq_flxd(a[2],a[3]))
