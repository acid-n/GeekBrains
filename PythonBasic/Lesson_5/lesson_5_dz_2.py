# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# строки
lines = 0

# слова
words = 0

# буквы
letters = 0

# открываем файл и считаем строки, слова и буквы
with open("file_5_2.txt") as f_obj:
    for line in f_obj:
        lines += 1
        letters += len(line)
        words += len(line.split())
        print(f"В {lines} строке {len(line.split())} слов и {len(line)} символов")

    print(f"Всего строк: {lines}")
    print(f"Всего слов: {words}")
    print(f"Всего символов: {letters}")
