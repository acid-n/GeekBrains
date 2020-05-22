#  В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
#  Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min_id = 0
max_id = 0
for i in range(1, SIZE):
    if array[i] < array[min_id]:
        min_id = i
    elif array[i] > array[max_id]:
        max_id = i

print(f"Минимальный элемент массива: {array[min_id]}")
print(f"Максимальный элемент массива: {array[max_id]}")

if min_id > max_id:
    min_id, max_id = max_id, min_id

summa = 0
for i in range(min_id+1, max_id):
    summa += array[i]

print(f"Сумма элементов между ними: {summa}")