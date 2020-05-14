# По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
# Ссылка на схему https://drive.google.com/file/d/1YiI1pfvZd4rJQ8aIfogcJZZdyPGVD_Ps/view?usp=sharing


print("Введите координаты точки A(x1;y1):")
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))

print("Введите координаты точки B(x2;y2):")
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))

print("Уравнение прямой, проходящей через эти точки:")

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f" y = {k} * x + {b}")
