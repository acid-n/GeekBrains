#  Написать два алгоритма нахождения i-го по счёту простого числа.
#  Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
#  Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import math
import timeit
import cProfile

# Решета Эратосфена

# n = 10000
#
# sieve = [i for i in range(n)]
# print(sieve)
# sieve[1] = 0
#
# for i in range(2, n):
#     if sieve[i] != 0:
#         j = i + i
#         while j < n:
#             sieve[j] = 0
#             j += i
#
# print(sieve)
# res = [i for i in sieve if i != 0]
# print(res)

#  Вариант 1

def func_(x):
    n = x * math.log2(x)
    n = int(n) + 5 # сделал такой ход, чтобы избежать ошибки при малом запрошенном числе
    sieve = [i for i in range(n)]  # квадратные скобки (массив) в рамках алгоритма, но не для использования в ПЗ
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return f'sieve({x}) -> простое число {res[x - 1]}'

print(func_(10100))


# Вариант 2

def sieve_(x):
    new_sieve = []
    rng = 100
    start = 2
    while True:
        for i in range(start, rng):
            if i % 2 != 0 and i % 3 != 0 and i % 4 != 0 and i % 5 != 0 and i % 6 != 0 and i % 7 != 0 and i % 8 != 0 \
                    and i % 9 != 0 or i == 2 or i == 3 or i == 5 or i == 7:
                new_sieve.append(i)
            start = i
        rng += 100
        if len(new_sieve) >= x:
            return f'sieve({x}) -> простое число {new_sieve[x - 1]}'


print(sieve_(10100))

# Тестирование

# Вариант 1
print("\nТест #1 TiemeIt")
print(timeit.timeit('func_(1000)', number=100, globals=globals()))      # 0.21428569999989122
print(timeit.timeit('func_(10000)', number=100, globals=globals()))     # 3.239479356998345
print(timeit.timeit('func_(100000)', number=100, globals=globals()))    # 59.60839975000272

print("\nТест #1 cProfile")
cProfile.run('func_(1000)')
# 7 function calls in 0.002 seconds
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 les_4_task_2.py:37(func_)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:40(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:49(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log2}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('func_(10000)')
# 7 function calls in 0.037 seconds
#         1    0.001    0.001    0.037    0.037 <string>:1(<module>)
#         1    0.029    0.029    0.036    0.036 les_4_task_2.py:37(func_)
#         1    0.004    0.004    0.004    0.004 les_4_task_2.py:40(<listcomp>)
#         1    0.003    0.003    0.003    0.003 les_4_task_2.py:49(<listcomp>)
#         1    0.000    0.000    0.037    0.037 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log2}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('func_(100000)')
# 7 function calls in 0.625 seconds
#         1    0.010    0.010    0.625    0.625 <string>:1(<module>)
#         1    0.516    0.516    0.614    0.614 les_4_task_2.py:37(func_)
#         1    0.062    0.062    0.062    0.062 les_4_task_2.py:40(<listcomp>)
#         1    0.036    0.036    0.036    0.036 les_4_task_2.py:49(<listcomp>)
#         1    0.000    0.000    0.625    0.625 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log2}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариант 2
print("\nТест #2 TiemeIt")
print(timeit.timeit('sieve_(1000)', number=100, globals=globals()))      # 0.07967994899809128
print(timeit.timeit('sieve_(10000)', number=100, globals=globals()))     # 0.8577174469974125
print(timeit.timeit('sieve_(100000)', number=100, globals=globals()))    # 8.759561651000695

print("\nТест #2 cProfile")
cProfile.run('sieve_(1000)')
# 1056 function calls in 0.001 seconds
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 les_4_task_2.py:57(sieve_)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        43    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1009    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('sieve_(10000)')
# 10438 function calls in 0.010 seconds
#         1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#         1    0.010    0.010    0.010    0.010 les_4_task_2.py:57(sieve_)
#         1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#       427    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     10007    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('sieve_(100000)')
# 104292 function calls in 0.098 seconds
#         1    0.001    0.001    0.098    0.098 <string>:1(<module>)
#         1    0.092    0.092    0.097    0.097 les_4_task_2.py:57(sieve_)
#         1    0.000    0.000    0.098    0.098 {built-in method builtins.exec}
#      4269    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    100019    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}