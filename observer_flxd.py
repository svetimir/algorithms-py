#шаблон наблюдатель
#пример реализации

#Georgy Yashin, ifi@yandex.ru
#2.9.2017

import weakref

class Account(object):
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.observers=set()
    def __del__(self):
        for ob in self.observers:
            ob.close()
        del self.observers
    def register(self,observer):
        self.observers.add(observer)
    def unregister(self,observer):
        self.observers.remove(observer)
    def notify(self):
        for ob in self.observers:
            ob.update()
    def withdraw(self,amt):
        self.balance-=amt
        self.notify()

class AccountObserver(object):
    def __init__(self,theaccount):
        self.accountref=weakref.ref(theaccount)
        theaccount.register(self)
    def __del__(self):
        acc=self.accountref()
        if acc:
            acc.unregister(self)
    def update(self):
        print("Баланс: %0.2f"%self.accountref().balance)
    def close(self):
        print("Наблюдение за счетом окончено")

a=Account("Dave",1000.0)
a_ob=AccountObserver(a)
a.withdraw(100)
