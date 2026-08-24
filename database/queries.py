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
