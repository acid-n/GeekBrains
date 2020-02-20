# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import re
import json

a = []
b = {}
sum_list = []

# открываем файл, считываем данные
with open("file_5_7.txt") as out_f:
    for i in out_f.readlines():
        # применяем регулярное выражение для поиска цифр в строке и преобразуем в int
        k = [int(s) for s in re.findall(r'\b\d+\b', i)]
        rz = k[0] - k[1]
        sum_list.append(rz)
        a = i.split()
        c = a[0]
        b[c] = rz

avar_pr = {}
avar_pr["avarage_profit"] = sum(sum_list) / len(b)
js_list = []
js_list.append(b)
js_list.append(avar_pr)
print(js_list)

with open("file_5_7_json.json", "w") as write_f:
    json.dump(js_list, write_f, ensure_ascii=False, indent=4)