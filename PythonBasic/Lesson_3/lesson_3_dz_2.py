# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
def data_people(arg_name, arg_surname, arg_date, arg_city, arg_email, arg_phone):
    return f"Ваше имя {arg_name}, фамилия {arg_surname}. Вы родились {arg_date}. Проживаете в городе {arg_city}. Ваш email: {arg_email}. Ваш телефон: {arg_phone}"

name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
date = input("Введите вашу дату рождения: ")
city = input("Введите ваш город проживания: ")
email = input("Введите ваш email: ")
phone = input("Введите ваш телефон: ")


print(data_people(arg_name=name, arg_surname=surname, arg_date=date, arg_city=city, arg_email=email, arg_phone=phone))