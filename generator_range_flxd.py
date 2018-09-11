# -*- coding: utf-8 -*-

# функция-генератор для создания списков
# с вещественными числами
# код генератора взят с stackoverflow
# табулируемая функция задается интегралом

# AUTHOR: Georgy Yashin, ifi@yandex.ru
# DATE: 04.09.2017
# LATEST REVISION: 08.09.2018

import math

# для рисования графика
import matplotlib.pyplot as plt
import scipy.integrate as ig
import numpy as np

def drange(start,stop,step):
    """функция-генератор списка"""
    r=start
    while r<stop:
        yield r
        r+=step

def f(x):
    """0.1"""
    return math.exp(-x**2)

def g(x):
    """non elementary function"""
    y,err=ig.quad(f,-10,x)
    return y

if __name__=="__main__":
    xmin=-5.0
    xmax=5.0
    n=500
    dx=(xmax-xmin)/n
# табулируем функцию в пределах xmin,xmax
    print("testing "+drange.__name__)
    xi=drange(xmin,xmax,dx)
    a=[g(x) for x in xi]
    print(a)
    plt.plot(a)
    plt.show()
