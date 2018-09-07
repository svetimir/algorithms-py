# fluxoid, ifi@yandex.ru
# 27.6.2017
# Решаем задачу перебором делителей
# функция возвращает 1 если число простое
# и 0 если составное

import math

def is_prime(a):
    tol=1e-3
    if a==2:
        return 1
    for i in range(2,math.ceil(math.sqrt(a))+1):
        # перебор делителей в цикле
        if math.fmod(a,i) < tol:
            # составное число
            return 0
    else:
        # простое число
        return 1

# Определим все простые числа от x1 до x2

x1=1
x2=100
for i in range(x1,x2):
    if is_prime(i)==1:
        print('%d - простое число' % i);
