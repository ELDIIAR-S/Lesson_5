import sqlite3

from database.queries import (
    CREATE_FILMS_TABLE,
    CREATE_FILM_INFO_TABLE,
    INSERT_FILM,
    INSERT_FILM_INFO,
    GET_FILMS_JOIN
)


DB_NAME = "bot.db"


def connect_db():
    return sqlite3.connect(DB_NAME)



def create_table():

    db = connect_db()
    cursor = db.cursor()

    cursor.execute(CREATE_FILMS_TABLE)
    cursor.execute(CREATE_FILM_INFO_TABLE)

    db.commit()
    db.close()



def add_film(title, genre, rating):

    db = connect_db()
    cursor = db.cursor()

    cursor.execute(
        INSERT_FILM,
        (title, genre, rating)
    )

    film_id = cursor.lastrowid

    db.commit()
    db.close()

    return film_id



def add_film_info(film_id, year, country):

    db = connect_db()
    cursor = db.cursor()

    cursor.execute(
        INSERT_FILM_INFO,
        (
            film_id,
            year,
            country
        )
    )

    db.commit()
    db.close()



def get_films():

    db = connect_db()
    cursor = db.cursor()

    cursor.execute(GET_FILMS_JOIN)

    films = cursor.fetchall()

    db.close()

    return films