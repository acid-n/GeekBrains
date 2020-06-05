# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100].
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random
import timeit

# Генерируем массив для отображения
array = [random.randint(-100, 100) for _ in range(10)]

# Генерируем большой массив для теста скорости с помощью TimeIt
big_array = [random.randint(-10000, 10000) for _ in range(1000)]


# Сортировка пузырьком
def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


print("Сортировка пузырьком")
print(bubble_sort(array))


# Сортировка пузырьком с помощью for
def bubble_sort_2(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


print("Сортировка пузырьком с помощью for")
print(bubble_sort_2(array))


# Сортировка расчёской улучшает сортировку пузырьком (для теста)

def combsort(alist):
    alen = len(alist)
    gap = (alen * 10 // 13) if alen > 1 else 0
    while gap:
        if 8 < gap < 11:  # variant "comb-11"
            gap = 11
        swapped = False
        for i in range(alen - gap):
            if alist[i + gap] < alist[i]:
                alist[i], alist[i + gap] = alist[i + gap], alist[i]
                swapped = True
        gap = (gap * 10 // 13) or swapped
    return alist


print("Сортировка расчёской")
print(combsort(array))

# Смотрим скорость сортировки
print('*' * 50)
print("Проверяем сортировку с помощью TimeIt")
print(timeit.timeit('bubble_sort(big_array)', number=100, globals=globals()))  # 6.476047019001271
print(timeit.timeit('bubble_sort_2(big_array)', number=100, globals=globals()))  # 3.0041742579996935
print(timeit.timeit('combsort(big_array)', number=100, globals=globals()))  # 0.1234825279971119
