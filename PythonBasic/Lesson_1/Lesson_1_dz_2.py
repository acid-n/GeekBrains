# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# просим пользователя ввести секунды
user_time = int(input("Введите время в секундах: "))

#  получаем часы
hour = (user_time // 3600) % 24

# получаем минуты
minute = (user_time // 60) % 60

# получаем секунды
second = user_time % 60

# выводим в формате чч:мм:сс
print(f"Время {hour}:{minute}:{second}")

