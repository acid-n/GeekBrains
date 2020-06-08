# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9


from hashlib import sha1

string = input('Введите слово: ')

str_len = len(string)
sub_len = 1

sub_strings = []

while str_len > 1:
    for i in range(str_len):
        sub = sha1(string[i:i + sub_len].encode('utf-8')).hexdigest()
        if sub not in sub_strings:
            sub_strings.append(sub)
    sub_len += 1
    str_len -= 1

print(len(sub_strings))
