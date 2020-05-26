#  Проанализировать скорость и сложность одного любого алгоритма из разработанных
#  в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом
# (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.


# Задача 2 из 3 урока
#  Во втором массиве сохранить индексы четных элементов первого массива.
#  Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
#  второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
#  т.к. именно в этих позициях первого массива стоят четные числа.

import timeit
import cProfile
import random

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
print("Тест TIMEIT #1")
print(timeit.timeit('my_array(array_1, 10000)', number=100, globals=globals()))     # 0.07543561599595705
print(timeit.timeit('my_array(array_2, 100000)', number=100, globals=globals()))    # 0.7901111999963177
print(timeit.timeit('my_array(array_3, 1000000)', number=100, globals=globals()))   # 7.9769135899987305

print("\nТест cProfile #1")
cProfile.run('my_array(array_1, 1000)')
# 519 function calls in 0.000 seconds
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:34(my_array)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       515    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('my_array(array_2, 10000)')
# 4955 function calls in 0.001 seconds
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 les_4_task_1.py:34(my_array)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      4951    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('my_array(array_3, 100000)')
# 50035 function calls in 0.014 seconds
#         1    0.000    0.000    0.014    0.014 <string>:1(<module>)
#         1    0.011    0.011    0.013    0.013 les_4_task_1.py:34(my_array)
#         1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
#     50031    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Тест варианта №2
print("\nТест #2")
print(timeit.timeit('my_array2(array_1)', number=100, globals=globals()))  # 0.06527303899929393
print(timeit.timeit('my_array2(array_2)', number=100, globals=globals()))  # 0.6754265080016921
print(timeit.timeit('my_array2(array_3)', number=100, globals=globals()))  # 6.973672652995447

print("\nТест cProfile #2")
cProfile.run('my_array2(array_1)')
# 6 function calls in 0.001 seconds
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 les_4_task_1.py:46(my_array2)
#         1    0.001    0.001    0.001    0.001 les_4_task_1.py:47(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('my_array2(array_2)')
# 6 function calls in 0.007 seconds
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.000    0.000    0.007    0.007 les_4_task_1.py:46(my_array2)
#         1    0.007    0.007    0.007    0.007 les_4_task_1.py:47(<listcomp>)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('my_array2(array_3)')
# 6 function calls in 0.072 seconds
#         1    0.004    0.004    0.072    0.072 <string>:1(<module>)
#         1    0.000    0.000    0.068    0.068 les_4_task_1.py:46(my_array2)
#         1    0.068    0.068    0.068    0.068 les_4_task_1.py:47(<listcomp>)
#         1    0.000    0.000    0.072    0.072 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Тест варианта №3
print("\nТест #3")
print(timeit.timeit('my_array3(array_1)', number=100, globals=globals()))  # 0.13967405800212873
print(timeit.timeit('my_array3(array_2)', number=100, globals=globals()))  # 1.4060919789990294
print(timeit.timeit('my_array3(array_3)', number=100, globals=globals()))  # 14.324177496004268

print("\nТест cProfile #3")
cProfile.run('my_array3(array_1)')
# 15083 function calls in 0.003 seconds
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.002    0.002    0.003    0.003 les_4_task_1.py:52(my_array3)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#     10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#      5078    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('my_array3(array_2)')
# 150049 function calls in 0.029 seconds
#         1    0.000    0.000    0.029    0.029 <string>:1(<module>)
#         1    0.021    0.021    0.029    0.029 les_4_task_1.py:52(my_array3)
#         1    0.000    0.000    0.029    0.029 {built-in method builtins.exec}
#    100001    0.005    0.000    0.005    0.000 {built-in method builtins.len}
#     50044    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('my_array3(array_3)')
# 1499990 function calls in 0.299 seconds
#         1    0.004    0.004    0.299    0.299 <string>:1(<module>)
#         1    0.215    0.215    0.294    0.294 les_4_task_1.py:52(my_array3)
#         1    0.000    0.000    0.299    0.299 {built-in method builtins.exec}
#   1000001    0.057    0.000    0.057    0.000 {built-in method builtins.len}
#    499985    0.023    0.000    0.023    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Тест варианта №4
print("\nТест #4")
print(timeit.timeit('my_array4(array_1)', number=100, globals=globals()))    # 0.07675792800000636
print(timeit.timeit('my_array4(array_2)', number=100, globals=globals()))    # 0.790965292006149
print(timeit.timeit('my_array4(array_3)', number=100, globals=globals()))    # 8.186111949005863

print("\nТест cProfile #4")
cProfile.run('my_array4(array_1)')
# 5082 function calls in 0.001 seconds
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 les_4_task_1.py:67(my_array4)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      5078    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('my_array4(array_2)')
# 50048 function calls in 0.013 seconds
#         1    0.000    0.000    0.013    0.013 <string>:1(<module>)
#         1    0.011    0.011    0.013    0.013 les_4_task_1.py:67(my_array4)
#         1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
#     50044    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('my_array4(array_3)')
# 499989 function calls in 0.136 seconds
#         1    0.004    0.004    0.136    0.136 <string>:1(<module>)
#         1    0.109    0.109    0.132    0.132 les_4_task_1.py:67(my_array4)
#         1    0.000    0.000    0.136    0.136 {built-in method builtins.exec}
#    499985    0.022    0.000    0.022    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Выводы
# Вариант №2 оказался самым быстрым всех 3х тестах. Хотя на него не ставил ставку.
# Второе место у варианта №3, медленнее варианта №2, но быстрее всех остальных.