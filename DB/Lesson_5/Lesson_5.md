1) Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.
mysql> insert into users (created_at, updated_at) values (NOW(), NOW());
или
mysql> update users set created_at = NOW(), updated_at = NOW();

2) Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения в формате "20.10.2017 8:10". Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения.
mysql>update users set created_at = str_to_date(created_at, "%d.%m.%Y %k:%i"), updated_at = str_to_date(updated_at, "%d.%m.%Y %k:%i");
mysql>alter table users modify created_at, updated_at datetime;

3) В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, если товар закончился и выше нуля, если на складе имеются запасы. Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value. Однако, нулевые запасы должны выводиться в конце, после всех записей.
mysql> select value from storehouses_products order by case when value = 0 then 100 else value end;
скорее всего решение не верное, так как "намудрил с граничными значениями"... и совсем не понял как вывести сортировку вместе с другими столбцами

в чате разобрали решение.. оказалось все просто
mysql> select value from storehouses_products order by value = 0, value;

4) Подсчитайте средний возраст пользователей в таблице users
mysql> SELECT ROUND(AVG(YEAR(now())- YEAR(birthday_at)), 0) as "AVG" FROM users;

5) Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. Следует учесть, что необходимы дни недели текущего года, а не года рождения.
mysql> SELECT COUNT(*) AS total, DAYNAME(CONCAT('2020-',SUBSTRING(birthday, 6, 10))) AS day FROM profiles GROUP BY day ORDER BY total DESC;

