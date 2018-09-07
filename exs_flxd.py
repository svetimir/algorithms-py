#Упражнения из книги
#"Алгоритмы. Теория и практическое применение", Род Стивенс

#started 27.08.2017
#Georgy Yashin, ifi@yandex.ru

import math
import random

def f(x):
    pass;

#наибольший общий делитель
def gcd(a,b):
    while b>0.01:
        r=math.fmod(a,b)
        a=b
        b=r
    return a

#print(gcd(531441,120000))

def create_array(size):
    a=list()
    for i in range(0,size):
        a.insert(i,random.randint(0,10))
    return a

a=create_array(5)
print(a)

#проверка на дубликаты
def dub(a):
    j=0
    d=0
    for i in range(0,len(a)):
        for j in range(j+i,len(a)):
            if(a[i]==a[j]):
                d+=1
        j=0
    return d

print(dub(a))           

# рандомизация массива

#генерация массивов со случайными числами
def create_array(size): return [random.randint(0,10) for i in range(0,size)]

a,b=create_array(10),create_array(10)
print(a,b)

def randomize_array(a):
    for i in range(len(a)):
        j=random.randint(i,len(a)-1)
        tmp=a[i]
        a[i]=a[j]
        a[j]=tmp
    return a

print(randomize_array(a),randomize_array(b))
