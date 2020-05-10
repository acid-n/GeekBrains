USE boosty;

DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name varchar(80) NOT NULL,
  last_name varchar(80) NOT NULL,
  email varchar(120) NOT NULL,
  phone varchar(120) NOT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS profiles;

CREATE TABLE profiles (
  id SERIAL PRIMARY KEY,
  user_id BIGINT UNSIGNED UNIQUE NOT NULL,
  gender ENUM('male', 'female') NOT NULL,
  birthday DATE DEFAULT NULL,
  city VARCHAR(120) DEFAULT NULL,
  country VARCHAR(120) DEFAULT NULL,
  photo_id BIGINT UNSIGNED UNIQUE NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS stores;

CREATE TABLE stores (
  id SERIAL PRIMARY KEY,
  user_id BIGINT UNSIGNED UNIQUE NOT NULL
);

DROP TABLE IF EXISTS store_profiles;

CREATE TABLE store_profiles (
  id SERIAL PRIMARY KEY,
  store_id BIGINT UNSIGNED UNIQUE NOT NULL,
  store_url varchar(255) NOT NULL,
  img_back_store_id BIGINT UNSIGNED NOT NULL,
  info_store varchar(2000) DEFAULT NULL,
  link_youtube varchar(255) DEFAULT NULL,
  link_vk varchar(255) DEFAULT NULL,
  link_facebook varchar(255) DEFAULT NULL,
  link_ok varchar(255) DEFAULT NULL,
  link_twitter varchar(255) DEFAULT NULL,
  link_twitch varchar(255) DEFAULT NULL,
  link_instagram varchar(255) DEFAULT NULL,
  link_soundcloud varchar(255) DEFAULT NULL,
  link_dribble varchar(255) DEFAULT NULL,
  link_begance varchar(255) DEFAULT NULL,
  link_telegram varchar(255) DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS store_posts;

CREATE TABLE store_posts (
  id SERIAL PRIMARY KEY,
  store_id BIGINT UNSIGNED NOT NULL,
  head VARCHAR(80) NOT NULL,
  body VARCHAR(2000) NOT NULL,
  media_id BIGINT UNSIGNED DEFAULT NULL,
  link_video VARCHAR(255) DEFAULT NULL,
  link_audio VARCHAR(255) DEFAULT NULL,
  link VARCHAR(255) DEFAULT NULL,
  post_price DECIMAL(11,2) DEFAULT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS subscription_levels;

CREATE TABLE subscription_levels (
  id SERIAL PRIMARY KEY,
  store_id BIGINT UNSIGNED NOT NULL,
  name VARCHAR(100) NOT NULL,
  description VARCHAR(255) NOT NULL,
  price DECIMAL(11,2) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS media;

CREATE TABLE media (
  id SERIAL PRIMARY KEY,
  media_type_id INT UNSIGNED NOT NULL,
  user_id BIGINT UNSIGNED NOT NULL,
  file_path VARCHAR(255) NOT NULL,
  size INT NOT NULL,
  metadata JSON DEFAULT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS media_types;

CREATE TABLE media_types (
  id INT UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(80) NOT NULL
);

DROP TABLE IF EXISTS payments;

CREATE TABLE payments (
  id SERIAL PRIMARY KEY,
  order_id BIGINT UNSIGNED NOT NULL,
  payment_amount DECIMAL(11,2) DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id BIGINT UNSIGNED NOT NULL,
  store_id BIGINT UNSIGNED NOT NULL,
  subscription_level_id BIGINT UNSIGNED NOT NULL,
  subscription_level_price DECIMAL(11,2) NOT NULL,
  order_status_id INT UNSIGNED NOT NULL,
  order_details VARCHAR(255) DEFAULT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS order_statuses;

CREATE TABLE order_statuses (
  id INT UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS paid_subscriptions;

CREATE TABLE paid_subscriptions (
  id SERIAL PRIMARY KEY,
  user_id BIGINT UNSIGNED NOT NULL,
  subscription_level_id BIGINT UNSIGNED NOT NULL,
  order_id BIGINT UNSIGNED NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- Создаем внешние ключи

ALTER TABLE profiles ADD CONSTRAINT profiles_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE;
ALTER TABLE profiles ADD CONSTRAINT profiles_photo_id_fk FOREIGN KEY (photo_id) REFERENCES media (id);

ALTER TABLE stores ADD CONSTRAINT stores_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id);

ALTER TABLE store_profiles ADD CONSTRAINT store_profiles_store_id_fk FOREIGN KEY (store_id) REFERENCES stores (id);
ALTER TABLE store_profiles ADD CONSTRAINT store_profiles_img_back_store_id FOREIGN KEY (img_back_store_id) REFERENCES media (id);

ALTER TABLE store_posts ADD CONSTRAINT store_posts_store_id_fk FOREIGN KEY (store_id) REFERENCES stores (id);
ALTER TABLE store_posts ADD CONSTRAINT store_posts_media_id_fk FOREIGN KEY (media_id) REFERENCES media (id);

ALTER TABLE media ADD CONSTRAINT media_media_type_id_fk FOREIGN KEY (media_type_id) REFERENCES media_types (id);
ALTER TABLE media ADD CONSTRAINT media_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id);

ALTER TABLE subscription_levels ADD CONSTRAINT subscription_levels_store_id_fk FOREIGN KEY (store_id) REFERENCES stores (id);

ALTER TABLE orders ADD CONSTRAINT orders_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id);
ALTER TABLE orders ADD CONSTRAINT orders_store_id_fk FOREIGN KEY (store_id) REFERENCES stores (id);
ALTER TABLE orders ADD CONSTRAINT orders_order_status_id_fk FOREIGN KEY (order_status_id) REFERENCES order_statuses (id);

ALTER TABLE payments ADD CONSTRAINT payments_order_id_fk FOREIGN KEY (order_id) REFERENCES orders (id);

ALTER TABLE paid_subscriptions ADD CONSTRAINT paid_subscriptions_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id);
ALTER TABLE paid_subscriptions ADD CONSTRAINT paid_subscriptions_subscription_level_id_fk FOREIGN KEY (subscription_level_id) REFERENCES subscription_levels (id);
ALTER TABLE paid_subscriptions ADD CONSTRAINT paid_subscriptions_order_id_fk FOREIGN KEY (order_id) REFERENCES orders (id);


-- Создаем индексы

CREATE UNIQUE INDEX users_email_uq ON users(email);
CREATE UNIQUE INDEX users_phone_uq ON users(phone);
CREATE INDEX users_first_name_idx ON users(first_name);
CREATE INDEX users_last_name_idx ON users(last_name);
CREATE INDEX users_email_phone ON users(email, phone);

CREATE INDEX profiles_birthday_idx ON profiles(birthday);
CREATE INDEX profiles_city_idx ON profiles(city);
CREATE INDEX profiles_country_idx ON profiles(country);
CREATE INDEX profiles_gender_birthday ON profiles(gender, birthday);

CREATE INDEX media_media_type_id_idx ON media(media_type_id);
CREATE INDEX media_user_id_idx ON media(user_id);
CREATE INDEX media_file_path_idx ON media(file_path);
CREATE INDEX media_size_idx ON media(size);
CREATE INDEX media_media_type_id_user_id ON media(media_type_id, user_id);
CREATE INDEX media_media_type_id_size ON media(media_type_id, size);
CREATE INDEX media_media_type_id_file_path ON media(media_type_id, file_path);

CREATE INDEX stores_user_id_idx ON stores(user_id);

CREATE INDEX store_profiles_store_id_idx ON store_profiles(store_id);
CREATE INDEX store_profiles_store_url_idx ON store_profiles(store_url);
CREATE INDEX store_profiles_img_back_store_id_idx ON store_profiles(img_back_store_id);

CREATE INDEX store_posts_store_id_idx ON store_posts(store_id);
CREATE UNIQUE INDEX store_posts_head_uq ON store_posts(head);
CREATE INDEX store_posts_media_id_idx ON store_posts(media_id);

CREATE INDEX subscription_levels_store_id_idx ON subscription_levels(store_id);
CREATE INDEX subscription_levels_name_idx ON subscription_levels(name);

CREATE INDEX payments_order_id_idx ON payments(order_id);

CREATE INDEX orders_user_id_idx ON orders(user_id);
CREATE INDEX orders_store_id_idx ON orders(store_id);
CREATE INDEX orders_subscription_level_id_idx ON orders(subscription_level_id);
CREATE INDEX orders_order_status_id_idx ON orders(order_status_id);

CREATE INDEX order_statuses_name_idx ON order_statuses(name);

