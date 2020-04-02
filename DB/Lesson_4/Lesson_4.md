1) Повторить все действия по доработке БД vk.

Обновил в таблице users только телефоны (чтобы было приближено к реалиям)
UPDATE users SET phone = CONCAT("+7-", FLOOR(100 + RAND() * 899), "-", FLOOR(100 + RAND() * 899), "-",
    FLOOR(10 + RAND() * 89), "-", FLOOR(10 + RAND() * 89));


Обновил таблицу media_types:
TRUNCATE media_types;
INSERT INTO media_types (name) VALUES ('photo'), ('video'), ('audio');

Обновил в таблице media столбец media_type_id
UPDATE media SET media_type_id = FLOOR(1 + RAND() * 3);

возникла странность: эта команда в графической оболочке вызывала ошибку, в консоли отлично все прошло. Не понятно.

Обновил в таблице media столбец file_path
UPDATE media SET file_path = CONCAT('https://dropbox.com/vk/file_', FLOOR(1 + RAND() * 9899), '.jpg');

и тоже возникла ошибка, а через консоль все отлично получилось. Странности.

Обновил в таблице media столбец size
UPDATE media SET size = FLOOR(99999 + RAND() * 9999899);

и тоже возникла ошибка, а через консоль все отлично получилось.

Обновил в таблице media столбец metadata
UPDATE media SET metadata = CONCAT('{"owner":"', (SELECT CONCAT(first_name, ' ', last_name) FROM users WHERE id = user_id), '"}');

тут также возникла проблема в графической оболочке, пришлось через консколь

Обновил в таблице media столбец metadata
ALTER TABLE media MODIFY COLUMN metadata JSON;

Обновил таблицу friendship_statuses
TRUNCATE friendship_statuses;
INSERT INTO friendship_statuses (name) VALUES ('Requested'), ('Confirmed'), ('Rejected');

Удалил лишние группы в таблице communities
DELETE FROM communities WHERE id > 20;

Обновил таблицу communities_users
UPDATE communities_users SET community_id = FLOOR(1 + RAND() * 20);


