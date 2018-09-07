# нахождение наибольшего общего делителя
# алгоритм Евклида

# Georgy Yashin, ifi@yandex.ru
# 28.08.2017

import math

def euq_flxd(a,b):
    r=0
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

print(euq_flxd(4851,3003))
print(euq_flxd(531441,12))
