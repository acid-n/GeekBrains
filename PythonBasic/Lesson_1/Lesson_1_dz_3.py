# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# запрашиваем у пользователя число
n = input("Введите число: ")

# суммируем две строки
nn = n + n

# суммируем три строки
nnn = n + n + n

# переводим строку в число и суммируем между собой
number = int(n) + int(nn) + int(nnn)

# выводим сумму
print(number)

