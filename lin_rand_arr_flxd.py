#генерация массива псевдослучайных чисел заданного размера

#Georgy Yashin, ifi@yandex.ru
#28.08.2017

import math
import time

m=32768
a=23
b=12345

def lin_rand_arr_flxd(seed,size):
    if size==1:
        return math.ceil(math.fmod(a*math.ceil(seed)+b,m))
    r=[0 for i in range(size)]
    r[0]=math.ceil(seed)
    for i in range(1,size):
        r[i]=math.ceil(math.fmod((a*r[i-1]+b),m))
    return r[1:size]

print(lin_rand_arr_flxd(time.time(),10))
