# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# Ссылка на схему https://drive.google.com/file/d/1YiI1pfvZd4rJQ8aIfogcJZZdyPGVD_Ps/view?usp=sharing

a = ord(input('Введите 1-ю букву: '))
b = ord(input('Введите 2-ю букву: '))

a = a - ord('a') + 1
b = b - ord('a') + 1

print(f'Позиции: {a} и {b}')
print(f'Между буквами символов: {abs(a - b) - 1}')