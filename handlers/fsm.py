from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


from database.main_db import (
    add_film,
    add_film_info,
    get_films
)


router = Router()



class FilmForm(StatesGroup):

    title = State()
    genre = State()
    rating = State()

    year = State()
    country = State()



@router.message(Command("form"))
async def start_form(message: Message, state: FSMContext):

    await state.set_state(FilmForm.title)

    await message.answer(
        "Введите название фильма:"
    )



@router.message(FilmForm.title)
async def get_title(message: Message, state: FSMContext):

    await state.update_data(
        title=message.text
    )

    await state.set_state(
        FilmForm.genre
    )

    await message.answer(
        "Введите жанр:"
    )



@router.message(FilmForm.genre)
async def get_genre(message: Message, state: FSMContext):

    await state.update_data(
        genre=message.text
    )

    await state.set_state(
        FilmForm.rating
    )

    await message.answer(
        "Введите оценку от 1 до 10:"
    )



@router.message(FilmForm.rating)
async def get_rating(message: Message, state:FSMContext):

    if not message.text.isdigit():

        await message.answer(
            "Оценка должна быть числом"
        )

        return


    await state.update_data(
        rating=int(message.text)
    )


    await state.set_state(
        FilmForm.year
    )


    await message.answer(
        "Введите год выпуска:"
    )



@router.message(FilmForm.year)
async def get_year(message: Message, state:FSMContext):

    if not message.text.isdigit():

        await message.answer(
            "Введите число"
        )

        return


    await state.update_data(
        year=int(message.text)
    )


    await state.set_state(
        FilmForm.country
    )


    await message.answer(
        "Введите страну:"
    )



@router.message(FilmForm.country)
async def get_country(message: Message, state:FSMContext):

    await state.update_data(
        country=message.text
    )


    data = await state.get_data()


    # первая таблица
    film_id = add_film(
        data["title"],
        data["genre"],
        data["rating"]
    )


    # вторая таблица
    # общий ключ film_id записывается сюда
    add_film_info(
        film_id,
        data["year"],
        data["country"]
    )


    await message.answer(
        f"""
Фильм добавлен:

Название: {data['title']}
Жанр: {data['genre']}
Оценка: {data['rating']}
Год: {data['year']}
Страна: {data['country']}
        """
    )


    await state.clear()



@router.message(Command("films"))
async def show_films(message: Message):

    films = get_films()


    if not films:

        await message.answer(
            "Фильмов нет"
        )

        return


    text = "Список фильмов:\n\n"


    for film in films:

        text += (
            f" {film[1]}\n"
            f"Жанр: {film[2]}\n"
            f"Оценка: {film[3]}\n"
            f"Год: {film[4]}\n"
            f"Страна: {film[5]}\n\n"
        )


    await message.answer(text)