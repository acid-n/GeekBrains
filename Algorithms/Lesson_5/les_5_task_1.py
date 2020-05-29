# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter


# Фунция ввода прибыли за 4 квартала, на входе принимает пустой массив, на выходе заполненный массив
def profit_company(array):
    i = 1
    while i < 5:
        profit_company = int(input(f"Введите прибыль за {i}й квартал:  "))
        array[i] = profit_company
        i += 1
    return array


# Заполняем первую компанию
company_1 = input("Введите название первой компании: ")
prof_comp_1 = {}
a = profit_company(prof_comp_1)
sum_company_1 = sum(Counter.values(a))

# Заполняем вторую компанию
company_2 = input("Введите название второй компании: ")
prof_comp_2 = {}
b = profit_company(prof_comp_2)
sum_company_2 = sum(Counter.values(b))

print("*" * 50)

# Считаем среднюю прибыль по двум компаниям за год
avarage = (sum_company_1 + sum_company_2) / 2
print(f"Средняя прибыль за год двух компаний: {avarage}")

# Выводим наименование убыточного и прибыльного предприятия
if sum_company_1 < sum_company_2:
    print(f"Компания {company_1} убыточна.")
    print(f"Компания {company_2} прибыльная.")
else:
    print(f"Компания {company_1} прибыльная.")
    print(f"Компания {company_2} убыточная.")
