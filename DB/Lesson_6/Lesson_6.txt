1. Проанализировать запросы, которые выполнялись на занятии, определить возможные корректировки и/или улучшения (JOIN пока не применять). Создать таблицы лайков и постов.
Сделал все, что на уроке делали, и вот еще осталось доделать связи (времени не хватило, все ушло на задачи с выбором)

ALTER TABLE posts
    ADD CONSTRAINT posts_user_id_fk
    FOREIGN KEY (user_id) REFERENCES users(id),
    ADD CONSTRAINT posts_community_id_fk
    FOREIGN KEY (community_id) REFERENCES communities(id),
    ADD CONSTRAINT posts_media_id_fk
    FOREIGN KEY (media_id) REFERENCES media(id);

ALTER TABLE messages
        ADD CONSTRAINT messages_from_user_id_fk
        FOREIGN KEY (from_user_id) REFERENCES users(id),
        ADD CONSTRAINT messages_to_user_id_fk
        FOREIGN KEY (to_user_id) REFERENCES users(id);

ALTER TABLE media
    ADD CONSTRAINT media_media_type_id_fk
    FOREIGN KEY (media_type_id) REFERENCES media_types(id),
    ADD CONSTRAINT media_user_id_fk
    FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE likes
    ADD CONSTRAINT likes_user_id_fk
    FOREIGN KEY (user_id) REFERENCES users(id),
    ADD CONSTRAINT likes_target_type_id_fk
    FOREIGN KEY (target_type_id) REFERENCES target_types(id);

ALTER TABLE friendship
    ADD CONSTRAINT friendship_user_id_fk
        FOREIGN KEY (user_id) REFERENCES users(id),
    ADD CONSTRAINT friendship_friend_id_fk
        FOREIGN KEY (friend_id) REFERENCES users(id),
    ADD CONSTRAINT friendship_status_id_fk
        FOREIGN KEY (status_id) REFERENCES friendship_statuses(id);

ALTER TABLE communities_users
    ADD CONSTRAINT communities_users_community_id_fk
        FOREIGN KEY (community_id) REFERENCES communities(id),
    ADD CONSTRAINT communities_users_user_id_fk
        FOREIGN KEY (user_id) REFERENCES users(id);


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


