# числа фибоначчи за O(N)
# если совсем честно, то алгоритм чуть медленнее, чем O(N)
# из-за сложения очень больших чисел
# а именно O(N**2) на больших N

# Georgy Yashin, ifi@yandex.ru
# 06.09.2017

import timeit

# массив чисел фибоначчи
def fib_array_flxd(n):
    if n==0: return [0]
    elif n==1: return [0,1]
    f=list()
    f.append(0)
    f.append(1)
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f

# print(fib_array_flxd(10))

def fib_array_2_flxd(n):
    if n==0: return [0]
    elif n==1: return [0,1]
    f=[0 for i in range(n+1)]
    f[0]=0
    f[1]=1
    for i in range(2,n+1):
        f[i]=f[i-1]+f[i-2]
    return f

# print(fib_array_2_flxd(10))

# заданное n-ное число фибоначчи
def fib_num_flxd(n):
    if n==0: return 0
    elif n==1: return 1
    fmin1=1
    fmin2=0
    f=0
    for i in range(2,n+1):
        f=fmin1+fmin2
        fmin2,fmin1=fmin1,f
    return f

# print(fib_num_flxd(500))

# золотое сечение
def golden_sect_flxd(n):
    if n>=2: return fib_num_flxd(n-1)/fib_num_flxd(n)
    else: return 0

# print(golden_sect_flxd(500))

# проверяем скорость работы функций
nt=10000
t1=timeit.Timer('fib_array_flxd(50)',setup='from __main__ import fib_array_flxd')
t2=timeit.Timer('fib_array_2_flxd(50)',setup='from __main__ import fib_array_2_flxd')
t3=timeit.Timer('fib_num_flxd(50)',setup='from __main__ import fib_num_flxd')
t4=timeit.Timer('golden_sect_flxd(50)',setup='from __main__ import golden_sect_flxd')

for i in range(4):
    print('fib_array_flxd(50)')
    print(t1.timeit(nt))
    print('fib_array_2_flxd(50)')
    print(t2.timeit(nt))
    print('fib_num_flxd(50)')
    print(t3.timeit(nt))
    print('golden_sect_flxd(50)')
    print(t4.timeit(nt))
    print("next step...\n")

# print(fib_num_flxd(10000))
# print(timeit.timeit('fib_num_flxd(10000)',setup='from __main__ import fib_num_flxd',number=1))
