#   AUTHOR: fluxoid, ifi@yandex.ru
#   VERSION: 0.0.1
#   LATEST REVISION: 05.09.2018
#   DESCRIPTION: Функции квадратичных сортировок массивов
#   PURPOSES: Educational

# вставками
def insert_sort():
    pass

# выбором
def choice_sort():
    pass

# пузырьком
def bubble_sort():
    pass

def test_sort(sort_algorithm):
    print("testcase #1: ",end="")
    A=[4,2,5,1,3]
    A_sorted=[1,2,3,4,5]
    sort_algorithm(A)
    print("Ok" if A==A_sorted else "Fail")

    print("testcase #2: ",end="")
    A=list(range(10,20))+list(range(0,10))
    A_sorted=list(range(20))
    sort_algorithm(A)
    print("Ok" if A==A_sorted else "Fail")

    print("testcase #3: ",end="")
    A=[4,2,4,2,1]
    A_sorted=[1,2,2,4,4]
    sort_algorithm(A)
    print("Ok" if A==A_sorted else "Fail")

    
if __name__ == "__main__":
    test_sort()
