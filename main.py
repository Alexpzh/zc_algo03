import time
import numpy as np
import timeit

a = np.random.randint(-100000, 100000, 10000)
print(a)

#   Пузырьковая сортировка (Bubble Sort);
def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

b = []
b = a.copy()

tt0 = time.time()
bubble_sort(b)
tt1 = time.time()

print('Сортировка пузырьком: ', tt1 - tt0)
print(b)



#   Сортировка выбором (Selection Sort);
#   Быстрая сортировка (Quick Sort);

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

b = []
b = a.copy()

tt0 = time.time()
quick_sort(b)
tt1 = time.time()

print('Быстрая сортировка: ', tt1 - tt0)
print(b)

#   Сортировка слиянием (Merge Sort)

#inp = input("Enter number: ")

#a = [-3, 5, 0, -8, 1, 10]

#   Сортировка вставками (Insertion Sort);
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


b = []
b = a.copy()

tt0 = time.time()
insert_sort(b)
tt1 = time.time()

print('Сортировка вставками: ', tt1 - tt0)
print(b)
# Результат: [-8, -3, 0, 1, 5, 10]
bb = []
bb = a.copy()
bb.sort()

print (b-bb)

