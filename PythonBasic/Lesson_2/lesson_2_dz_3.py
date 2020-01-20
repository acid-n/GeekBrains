# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# словарь времеи года
season = {'Winter': ('1', '2', '12'), 'Spring': ('3', '4', '5'), 'Summer': ('6', '7', '8'), 'Autumn': ('9', '10', '11')}

# Пользователь вводит число
month = input("Введите месяц года числом: ")

# выводим время года в зависимости от введенного числа
for x in season:
    if month in season[x]:
        print(x)

# Список времен года
season_list = ('Winter', 'Spring', 'Summer', 'Autumn')
month = int(month)

if month == 1 or month == 2 or month == 12:
    print(season_list[0])
elif month == 3 or month == 4 or month == 5:
    print(season_list[1])
elif month == 6 or month == 7 or month == 8:
    print(season_list[2])
elif month == 9 or month == 10 or month == 11:
    print(season_list[3])

