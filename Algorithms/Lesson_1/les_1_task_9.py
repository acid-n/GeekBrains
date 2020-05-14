# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# Ссылка на схему https://drive.google.com/file/d/1YiI1pfvZd4rJQ8aIfogcJZZdyPGVD_Ps/view?usp=sharing

print('Введите три числа')
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

if b < a < c or c < a < b:
    print(f'Среднее: {a}')
elif a < b < c or c < b < a:
    print(f'Среднее: {b}')
else:
    print(f'Среднее: {c}')