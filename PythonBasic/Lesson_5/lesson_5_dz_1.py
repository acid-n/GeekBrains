# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


def my_write_file(my_string):
    with open("my_text_file.txt", "a") as out_f:
        out_f.write(my_string)


while True:
    a = input('Введите слово (чтобы завершить, оставьте пустую строку и нажмите Enter): ')
    if a == '':
        break
    else:
        b = a + '\n'
        my_write_file(b)
