# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# Создадим словарь с английскими названиями цифр
en_numbers = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
              10: 'Ten'}

# Создадим словарь с русскими названиями цифр
ru_numbers = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыри', 5: 'Пять', 6: 'Шесть', 7: 'Семь', 8: 'Восемь', 9: 'Девять',
              10: 'Десять'}


# открываем файл и считываем строки, получаем ключ,
# по ключу берем значение из русского словаря и записываем в новый файл
with open("file_5_4.txt") as f_obj:
    for line in f_obj:
        a = line.split()
        c = int(a[2])
        with open("file_5_4__a.txt", "a") as w_obj:
            w_obj.writelines(f"{ru_numbers[c]} - {c}\n")
