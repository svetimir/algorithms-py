#рандомизация массива

#28.08.2017
#Georgy Yashin, ifi@yandex.ru

import random

#генерация массивов со случайными числами
def create_array_flxd(size): return [random.randint(0,10) for i in range(size)]

def randomize_array_flxd(a):
    for i in range(len(a)):
        j=random.randint(i,len(a)-1)
        tmp=a[i]
        a[i]=a[j]
        a[j]=tmp
    return a

a,b=create_array_flxd(10),create_array_flxd(10)

print(a,b)
print(randomize_array_flxd(a),randomize_array_flxd(b))
