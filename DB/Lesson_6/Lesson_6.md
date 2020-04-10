1. Проанализировать запросы, которые выполнялись на занятии, определить возможные корректировки и/или улучшения (JOIN пока не применять). Создать таблицы лайков и постов.
Сделал все, что на уроке делали, и вот еще осталось доделать связи (времени не хватило, все ушло на задачи с выбором)

2. Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей.
SELECT
    (SELECT CONCAT(first_name, ' ', last_name) FROM users where id = profiles.user_id) AS users,
    (SELECT COUNT(*) from likes where user_id = profiles.user_id) AS likes,
    birthday
    FROM profiles
    ORDER BY birthday DESC limit 10;

3. Определить кто больше поставил лайков (всего) - мужчины или женщины?
SELECT
    (SELECT SUM((SELECT COUNT(*) FROM likes WHERE user_id = profiles.user_id))
    FROM profiles where gender = 'm') AS m_likes,
    (SELECT SUM((SELECT COUNT(*) FROM likes WHERE user_id = profiles.user_id))
    FROM profiles where gender = 'f') AS f_likes
    FROM profiles limit 1;

4. Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети.
SELECT
    (SELECT CONCAT(first_name, ' ', last_name) FROM users where id = profiles.user_id) AS users,
    (
        (SELECT COUNT(*) from likes where user_id = profiles.user_id) +
        (SELECT COUNT(*) from media where user_id = profiles.user_id) +
        (SELECT COUNT(*) from messages where from_user_id = profiles.user_id)
    ) AS total
    FROM profiles
    ORDER BY total limit 10;


