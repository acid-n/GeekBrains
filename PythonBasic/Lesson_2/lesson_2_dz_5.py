# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Список формируем заранее
my_list = ['7', '5', '3', '3', '2']

# Ограничиваем цикл тремя проходами
x = 0

while x < 3:
    # Запрашиваем число у пользователя
    number = input("Введите число: ")
    # Уточняем есть ли такой элемент в нашем спике, если да, то
    if number in my_list:
        # Ищем позицию числа введенного пользователем
        list_position = my_list.index(number)
        # Вставляем к найденому числу
        my_list.insert(list_position, number)
    # если в нашем списке не нашли
    else:
        # добавляем в конец списка
        my_list.append(number)

    # сортируем наш обновленные не возрастающий список
    my_list = sorted(my_list, reverse=True)
    print(my_list)

    # увеличиваем счетчик нашего цикла
    x = x + 1
