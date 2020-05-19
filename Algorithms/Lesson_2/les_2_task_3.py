# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

# ссылка на схему https://drive.google.com/file/d/1NKj_9dP0PRgc3wKV1yTjp4gf5ANSyFnU/view?usp=sharing


def inverse_n(x):
    if len(str(x)) == 1:
        return f'{x}'
    elif len(str(x)) > 1:
        y = x % 10
        return f'{y}{inverse_n(x // 10)}'


n = int(input("Введите число: "))
m = inverse_n(n)
print(f"Вы ввели число {n}, сформированное обратное по порядку входящего {m}")