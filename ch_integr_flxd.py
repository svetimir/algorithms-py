# -*- coding: utf-8 -*-

# численное интегрирование

# AUTHOR: Georgy Yashin, ifi@yandex.ru
# DATE: 02.09.2017
# LATEST REVISION: 08.09.2018

import math

def fn(x):
    return math.sin(x)+math.cos(x)

# метод прямоугольников
def rect_integral(f,xmin,xmax,n):
    """процедура интегрирования по методу прямоугольников"""
    dx=(xmax-xmin)/n
    area=0
    x=xmin
    for i in range(n):
        area+=dx*f(x)
        x+=dx
    return area

# метод трапеций
def tr_integral(f,xmin,xmax,n):
    """процедура интегрирования по методу трапеций"""
    dx=(xmax-xmin)/n
    area=0
    x=xmin
    for i in range(n):
        area+=dx*(f(x)+f(x+dx))/2
        x+=dx
    return area

if __name__=="__main__":
    print("тестируем "+rect_integral.__doc__+":\n{}".format(rect_integral(fn,0,math.pi/4,10000)))
    print("тестируем "+tr_integral.__doc__+":\n{}".format(tr_integral(fn,0,math.pi/4,10000)))
