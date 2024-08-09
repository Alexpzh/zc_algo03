import time

import numpy as np
import timeit

a = np.random.randint(-1000, 1000, 10)
print(a)

#   Пузырьковая сортировка (Bubble Sort);
#   Сортировка выбором (Selection Sort);
#   Сортировка вставками (Insertion Sort);
#   Быстрая сортировка (Quick Sort);
#   Сортировка слиянием (Merge Sort)

inp = input("Enter number: ")

#a = [-3, 5, 0, -8, 1, 10]

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

tt0 = time.time()
insert_sort(a)
tt1 = time.time()

print('Сортировка вставками: ', tt1 - tt0)
print(a)
# Результат: [-8, -3, 0, 1, 5, 10]
b = a.sort()

print (b)

