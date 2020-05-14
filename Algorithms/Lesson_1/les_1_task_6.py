# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# Ссылка на схему https://drive.google.com/file/d/1YiI1pfvZd4rJQ8aIfogcJZZdyPGVD_Ps/view?usp=sharing

n = int(input('Введите номер буквы в алфавите: '))

n = ord('a') + n - 1

print(f'Это буква {chr(n)}')