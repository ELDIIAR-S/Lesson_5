CREATE_FILMS_TABLE = """
CREATE TABLE IF NOT EXISTS films (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    rating INTEGER NOT NULL
);
"""


CREATE_FILM_INFO_TABLE = """
CREATE TABLE IF NOT EXISTS film_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    film_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    country TEXT NOT NULL,

    FOREIGN KEY (film_id) REFERENCES films(id)
);
"""


INSERT_FILM = """
INSERT INTO films(title, genre, rating)
VALUES (?, ?, ?);
"""


INSERT_FILM_INFO = """
INSERT INTO film_info(film_id, year, country)
VALUES (?, ?, ?);
"""


GET_FILMS_JOIN = """
SELECT 
    films.id,
    films.title,
    films.genre,
    films.rating,
    film_info.year,
    film_info.country

FROM films

INNER JOIN film_info

ON films.id = film_info.film_id;
"""


