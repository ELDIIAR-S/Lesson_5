import sqlite3


from database.queries import (
    CREATE_PRODUCTS_TABLE,
    CREATE_PRODUCT_INFO_TABLE,

    INSERT_PRODUCT,
    INSERT_PRODUCT_INFO,

    GET_PRODUCTS_JOIN
)



DB_NAME = "bot.db"

# создание таблиц

async def create_table():

    db = sqlite3.connect(DB_NAME)

    cursor = db.cursor()


    cursor.execute(
        CREATE_PRODUCTS_TABLE
    )


    cursor.execute(
        CREATE_PRODUCT_INFO_TABLE
    )


    db.commit()

    db.close()


# добавление товара

async def add_product(
        article,
        name,
        price
):

    db = sqlite3.connect(DB_NAME)

    cursor = db.cursor()


    cursor.execute(
        INSERT_PRODUCT,
        (
            article,
            name,
            price
        )
    )


    db.commit()

    db.close()


# добавление информации товара

async def add_product_info(
        article,
        category,
        description
):

    db = sqlite3.connect(DB_NAME)

    cursor = db.cursor()


    cursor.execute(
        INSERT_PRODUCT_INFO,
        (
            article,
            category,
            description
        )
    )


    db.commit()

    db.close()


# получение товаров через INNER JOIN

async def get_products():

    db = sqlite3.connect(DB_NAME)

    cursor = db.cursor()


    cursor.execute(
        GET_PRODUCTS_JOIN
    )


    products = cursor.fetchall()


    db.close()


    return products