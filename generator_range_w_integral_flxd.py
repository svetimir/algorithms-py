#функция-генератор для создания
#списков с вещественными числами
#код генератора взят с stackoverflow

#Georgy Yashin, ifi@yandex.ru
#04.09.2017

import math
import ch_integr_flxd as ci

def drange(start,stop,step):
    r=start
    while r<stop:
        yield r
        r+=step

def f(x): return math.exp(-pow(x,2)+math.cos(x))

xmin=-10.0
xmax=10.0
n=200
dx=(xmax-xmin)/n

#табулируем функцию в пределах xmin,xmax
xi=drange(xmin,xmax,dx)
a=[f(x) for x in xi]
print(a)

#возьмем интеграл от f(x) на xmin,xmax методом трапеций
print(ci.tr_integral(f,xmin,xmax,n))
