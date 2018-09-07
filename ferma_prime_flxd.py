#тест простоты Ферма

#29.08.2017
#Georgy Yashin, ifi@yandex.ru

#вероятностный алгоритм
#формула вероятности обманщика Ферма
#1/(2**tests)
#при 100 тестах примерно 7.8e-31

import random, math

def ferma_prime_flxd(p,tests):
    if p<=3: return True
    for test in range(tests):
        n=random.randint(1,p)
        if math.fmod(math.pow(n,p-1),p)!=1: return False
        return True

for i in range(100):
    if ferma_prime_flxd(i,20000):
        print("prime number found - ",i)
    
