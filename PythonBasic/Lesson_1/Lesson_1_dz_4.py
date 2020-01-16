# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое число: "))

print(number // 100)

print((number % 100) // 10)

print(number % 10)

i = number

#for b in number:
#    print(b)

#while number > 0:
#    number // 10
#    print(number)