# Создание первой таблицы

CREATE_PRODUCTS_TABLE = """

CREATE TABLE IF NOT EXISTS products(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    article INTEGER UNIQUE,

    name TEXT,

    price INTEGER

);

"""

# Создание второй таблицы


CREATE_PRODUCT_INFO_TABLE = """

CREATE TABLE IF NOT EXISTS product_info(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    article INTEGER,

    category TEXT,

    description TEXT

);

"""
# Добавление товара

INSERT_PRODUCT = """

INSERT INTO products(
    article,
    name,
    price
)

VALUES (?, ?, ?);

"""
# Добавление информации


INSERT_PRODUCT_INFO = """

INSERT INTO product_info(
    article,
    category,
    description
)

VALUES (?, ?, ?);

"""

# INNER JOIN получение товаров

GET_PRODUCTS_JOIN = """

SELECT

products.article,
products.name,
products.price,

product_info.category,
product_info.description


FROM products


INNER JOIN product_info


ON products.article = product_info.article;


"""

# ===========================
# Пункт 4:
#
# Если добавить запись только в первую таблицу users,
# а во вторую таблицу user_info данные не добавить,
# то при выполнении команды списка эта запись НЕ появится.
#
# Причина:
# INNER JOIN показывает только те записи,
# у которых есть совпадение в обеих таблицах.
#
# Если у пользователя есть запись в users,
# но нет связанной записи в user_info,
# то INNER JOIN исключит её из результата.
# ===========================