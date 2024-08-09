import time
import numpy as np
import timeit

a = np.random.randint(-100000, 100000, 10000)
#a = [-3, 5, 0, -8, 1, 10]
print("\nИсходный массив: ")
print(a)
bb = a.copy()
bb.sort()

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

print('\nСортировка пузырьком: ', format(tt1 - tt0, '.4f'))
print(b)
print('Разница между сортировками: ')
print (b-bb)



#   Сортировка выбором (Selection Sort);
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

b = []
b = a.copy()

tt0 = time.time()
selection_sort(b)
tt1 = time.time()

print('\nСортировка выбором: ', format(tt1 - tt0, '.4f'))
print(b)
print('Разница между сортировками: ')
print (b-bb)

#   Быстрая сортировка (Quick Sort);
def quick_sort(s):
    if len(s) <= 1:
        return s
    element = s[0]
    left = list(filter(lambda i: i < element, s))
    center = [i for i in s if i == element]
    right = list(filter(lambda i: i > element, s))

    return quick_sort(left) + center + quick_sort(right)

b = []
b = a.copy()

tt0 = time.time()
b = quick_sort(b)
tt1 = time.time()

print('\nБыстрая сортировка: ', format(tt1 - tt0, '.4f'))
#print(b)
print('Разница между сортировками: ')
print (b-bb)



def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort2(less) + [pivot] + quick_sort2(greater)

b = []
b = a.copy()

tt0 = time.time()
b = quick_sort2(b)
tt1 = time.time()

print('\nБыстрая сортировка (list): ', format(tt1 - tt0, '.4f'))
#print(b)
print('Разница между сортировками: ')
print (b-bb)

#   Сортировка слиянием (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        r = len(arr) // 2
        left = arr[:r]
        right = arr[r:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

b = a.copy()
tt0 = time.time()
merge_sort(b)
tt1 = time.time()

print('\nСортировка слиянием: ', format(tt1 - tt0, '.4f'))
print(b)
print('Разница между сортировками: ')
print (b-bb)

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


b = a.copy()
tt0 = time.time()
insert_sort(b)
tt1 = time.time()

print('\nСортировка вставками: ', format(tt1 - tt0, '.4f'))
print(b)
# Результат: [-8, -3, 0, 1, 5, 10]

print('Разница между сортировками: ')
print (b-bb)

