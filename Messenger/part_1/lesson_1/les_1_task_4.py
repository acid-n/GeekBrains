"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = [
    'разработка',
    'администрирование',
    'protocol',
    'standard'
]

words_encode = []
words_decode = []

for w in words:
    enc_str = w.encode('utf-8')
    words_encode.append(enc_str)

count = 0
for w in words:
    print(f'Строка: {w}, зашифрованная строка: {words_encode[count]}')
    count += 1


for w in words_encode:
    dec_str = w.decode('utf-8')
    words_decode.append(dec_str)

count2 = 0
for w in words_decode:
    print(f'Зашифрованная строка: {words_encode[count2]}, расшифрованная строка: {w}')
    count2 += 1