-- Выведите все товары из таблицы products
SELECT * FROM products;

-- Выведите только название (name) и категорию (category) всех товаров из таблицы products
SELECT name, category FROM products;

-- Выведите список всех уникальных категорий товаров из таблицы products
SELECT DISTINCT category FROM products;

-- Выведите все товары из таблицы products, отсортированные по названию в алфавитном порядке
SELECT * FROM products ORDER BY name ASC;

-- Выведите все товары из таблицы products, отсортированные по названию в обратном алфавитном порядке
SELECT * FROM products ORDER BY name DESC;

-- Выведите первые 10 товаров из таблицы products
SELECT * FROM products LIMIT 10;

-- Выведите 10 товаров из таблицы products, начиная с 11-й записи
SELECT * FROM products LIMIT 10 OFFSET 10;

-- Выведите 5 случайных товаров из таблицы products
SELECT * FROM products ORDER BY RANDOM() LIMIT 5;

-- Выведите все категории товаров из таблицы products (без использования DISTINCT), отсортированные по алфавиту
SELECT category FROM products ORDER BY category ASC;

-- Выведите все товары из таблицы products, отсортированные сначала по категории, затем по названию
SELECT * FROM products ORDER BY category ASC, name ASC;