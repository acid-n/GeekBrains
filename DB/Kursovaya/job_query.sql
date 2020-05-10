USE boosty;

-- Обновляем столбец с телефонами пользователей (чтобы было похоже к боевым условиям)
UPDATE users SET phone = CONCAT("+7-", FLOOR(100 + RAND() * 899), "-", FLOOR(100 + RAND() * 899), "-", FLOOR(10 + RAND() * 89), "-", FLOOR(10 + RAND() * 89));


-- Скрипты характерных выборок 

-- пользователь заходит на страницу магазина, показываем информацию о магазине
-- выводим имя, фамилию, айди фотографии пользователя, фотографию подложки, информацию о магазине
SELECT users.first_name, users.last_name, profiles.photo_id, store_profiles.img_back_store_id, store_profiles.info_store
FROM users 
LEFT JOIN profiles ON profiles.user_id = users.id
LEFT JOIN stores ON stores.user_id = users.id
LEFT JOIN store_profiles ON store_profiles.store_id = stores.id
WHERE users.id = 12;

-- какие у магазина есть подписки
SELECT id, name, description, price FROM subscription_levels WHERE store_id = 4;


-- Представления

DROP VIEW IF EXISTS store_view;
CREATE VIEW store_view AS
SELECT users.first_name, users.last_name, profiles.photo_id, store_profiles.img_back_store_id, store_profiles.info_store
FROM users 
LEFT JOIN profiles ON profiles.user_id = users.id
LEFT JOIN stores ON stores.user_id = users.id
LEFT JOIN store_profiles ON store_profiles.store_id = stores.id;

SELECT * from store_view;

-- Хранимые процедуры

DROP PROCEDURE IF EXISTS show_store;

DELIMITER //
CREATE PROCEDURE show_store(IN user_id INT)
BEGIN
  SELECT users.first_name, users.last_name, profiles.photo_id, store_profiles.img_back_store_id, store_profiles.info_store
  FROM users 
  LEFT JOIN profiles ON profiles.user_id = users.id
  LEFT JOIN stores ON stores.user_id = users.id
  LEFT JOIN store_profiles ON store_profiles.store_id = stores.id
  WHERE users.id = user_id;
END //
DELIMITER ;

CALL show_store(12);

-- Триггеры

-- создаем триггер, который будет после вставки в таблицу payments менять в таблице orders статус на оплачен 
DELIMITER //
DROP TRIGGER IF EXISTS orders_status//
CREATE TRIGGER orders_status AFTER INSERT ON payments
FOR EACH ROW
BEGIN
  UPDATE orders SET order_status_id = 3 WHERE id = NEW.order_id;
END//
DELIMITER ;

-- создаем оплаты, при которой должен изменитьтся статус заказа на оплачен
INSERT INTO payments(order_id, payment_amount) VALUES
(1, 20.00), (2, 10.00), (3, 5.00), (4, 3.00), (5, 5.00), (6, 3.00), (7, 10.00), (8, 20.00), (9, 15.00), (10, 5.00);

