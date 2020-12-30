# БД и запросы на выборку

# Подключение библиотеки, соответсвующей типу требуемой базы данных
import os
import sqlite3

DB_OBJ = os.path.join(os.path.dirname(__file__), "demo.sqlite")

# Создание соединения с базой данных
# В данном случае это файл базы
CONN = sqlite3.connect(DB_OBJ)

# Создаем курсор - это специальный объект, который делает запросы и получает их результаты
CURSOR = CONN.cursor()

# Запрос на выборку
CURSOR.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")

RESULTS = CURSOR.fetchall()
RESULTS_2 = CURSOR.fetchall()

print(RESULTS)
print(RESULTS_2)

