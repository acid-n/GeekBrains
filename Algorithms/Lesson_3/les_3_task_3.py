#  В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

mn = 0
mx = 0
for i in range(SIZE):
    if array[i] < array[mn]:
        mn = i
    elif array[i] > array[mx]:
        mx = i
    print(f"array[{mn+1}] = {array[mn]} array[{mx+1}] = {array[mx]}")
    b = array[mn]
    array[mn] = array[mx]
    array[mx] = b

for i in range(SIZE):
    print(array[i], end=' ')