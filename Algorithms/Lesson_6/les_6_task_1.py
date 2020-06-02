# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

import sys
import random
import struct
import ctypes

#  Взял свои варианты задачи 2 из 3 урока
#  Во втором массиве сохранить индексы четных элементов первого массива.
#  Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
#  второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
#  т.к. именно в этих позициях первого массива стоят четные числа.

SIZE_1 = 10000
SIZE_2 = 100000
SIZE_3 = 1000000

MIN_ITEM = 0
MAX_ITEM = 100000

array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_1)]
array_2 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_2)]
array_3 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_3)]


def my_array(array, n):
    even = []

    for i in range(n):
        if array[i] % 2 == 0:
            even.append(i)

    return even


# Вариант 2

def my_array2(array):
    return [i for i in range(len(array)) if array[i] % 2 == 0]


# Вариант 3

def my_array3(array):
    even = []
    i = 0

    while i < len(array):
        if array[i] % 2 == 0:
            even.append(i)

        i += 1

    return even


# Вариант 4

def my_array4(array):
    even = []

    for id, item in enumerate(array):
        if item % 2 == 0:
            even.append(id)

    return even


# Тест варианта №1
print("\nТест GetSizeOf #1")
print(sys.getsizeof(my_array(array_1, 1000)))
print(sys.getsizeof(my_array(array_2, 10000)))
print(sys.getsizeof(my_array(array_3, 100000)))

# Тест варианта №2
print("\nТест GetSizeOf #2")
print(sys.getsizeof(my_array2(array_1)))
print(sys.getsizeof(my_array2(array_2)))
print(sys.getsizeof(my_array2(array_3)))

# Тест варианта №3
print("\nТест GetSizeOf #3")
print(sys.getsizeof(my_array3(array_1)))
print(sys.getsizeof(my_array3(array_2)))
print(sys.getsizeof(my_array3(array_3)))

# Тест варианта №4
print("\nТест GetSizeOf #4")
print(sys.getsizeof(my_array4(array_1)))
print(sys.getsizeof(my_array4(array_2)))
print(sys.getsizeof(my_array4(array_3)))

# Размер переменных
print("\nРазмер переменных")

print(f"Смотрим переменную SIZE_1: {SIZE_1}, размер {sys.getsizeof(SIZE_1)}")
print(f"Смотрим переменную SIZE_2: {SIZE_2}, размер {sys.getsizeof(SIZE_2)}")
print(f"Смотрим переменную SIZE_3: {SIZE_3}, размер {sys.getsizeof(SIZE_3)}")

print(f"Смотрим переменную MIN_ITEM: {MIN_ITEM}, размер {sys.getsizeof(MIN_ITEM)}")
print(f"Смотрим переменную MAX_ITEM: {MAX_ITEM}, размер {sys.getsizeof(MAX_ITEM)}")

print(f"Смотрим переменную array_1, размер {sys.getsizeof(array_1)}")
print(f"Смотрим переменную array_2, размер {sys.getsizeof(array_2)}")
print(f"Смотрим переменную array_3, размер {sys.getsizeof(array_3)}")

# Вариант с циклами

def my_size():
    sum_size = 0
    for k in globals():
        if '__' not in str(k) and str(k) != 'sys':
            print(f'Смотрим объект {k}, размер {sys.getsizeof(globals()[str(k)])} ')
            sum_size += sys.getsizeof(globals()[str(k)])

    for k in locals():
        print(f'Смотрим объект {k} = {locals()[str(k)]}, размер {sys.getsizeof(locals()[str(k)])} ')
        sum_size += sys.getsizeof(locals()[str(k)])

    print('*' * 50)
    print(f'Общий объем всех объектов: {sum_size} байт')

print(f"\nВариант с циклами")
my_size()



# Еще решил посмотреть переменные через ctypes и struct из урока
print('*' * 50)
print(f"Еще посмотрим переменную через ctypes и struct из урока.")
print(f"Адрес переменной SIZE_3 в памяти {id(SIZE_3)}")
print(f"Размер данной переменной {sys.getsizeof(SIZE_3)}")
print(f"Как данные выглядят в памяти {ctypes.string_at(id(SIZE_3), sys.getsizeof(SIZE_3))}")
print(f"Применим STRUCT: {struct.unpack('QQQQQQQ', ctypes.string_at(id(SIZE_3), sys.getsizeof(SIZE_3)))}")


# Вывод
# Система Ubuntu 20, 64bit, Intel Core i7,
# Через memory_profiler не стал делать, это дополнительный модуль
# С помощью getsize интересно и полезно смотреть размер данных.