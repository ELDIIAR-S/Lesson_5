from aiogram import Router

from aiogram.types import Message

from aiogram.filters import Command

from aiogram.fsm.context import FSMContext

from aiogram.fsm.state import StatesGroup, State


from database.main_db import (
    add_product,
    add_product_info
)


router = Router()

# Состояния анкеты

class ProductForm(StatesGroup):

    article = State()

    name = State()

    price = State()

    category = State()

    description = State()


# Запуск анкеты

@router.message(Command("form"))
async def start_form(
        message: Message,
        state: FSMContext
):

    await state.set_state(
        ProductForm.article
    )


    await message.answer(
        "Введите артикул товара:"
    )



# Артикул

@router.message(ProductForm.article)
async def get_article(
        message: Message,
        state: FSMContext
):

    if not message.text.isdigit():

        await message.answer(
            "Артикул должен быть числом"
        )

        return



    await state.update_data(
        article=int(message.text)
    )


    await state.set_state(
        ProductForm.name
    )


    await message.answer(
        "Введите название товара:"
    )



# Название

@router.message(ProductForm.name)
async def get_name(
        message: Message,
        state: FSMContext
):

    await state.update_data(
        name=message.text
    )


    await state.set_state(
        ProductForm.price
    )


    await message.answer(
        "Введите цену товара:"
    )



# Цена

@router.message(ProductForm.price)
async def get_price(
        message: Message,
        state: FSMContext
):

    if not message.text.isdigit():

        await message.answer(
            "Цена должна быть числом"
        )

        return



    await state.update_data(
        price=int(message.text)
    )


    await state.set_state(
        ProductForm.category
    )


    await message.answer(
        "Введите категорию товара:"
    )


# Категория

@router.message(ProductForm.category)
async def get_category(
        message: Message,
        state: FSMContext
):

    await state.update_data(
        category=message.text
    )


    await state.set_state(
        ProductForm.description
    )


    await message.answer(
        "Введите описание товара:"
    )



# Описание
# Последний шаг
# Сохранение в две таблицы

@router.message(ProductForm.description)
async def get_description(
        message: Message,
        state: FSMContext
):

    await state.update_data(
        description=message.text
    )


    data = await state.get_data()



    article = data["article"]

    name = data["name"]

    price = data["price"]

    category = data["category"]

    description = data["description"]




# Запись в первую таблицу products


    await add_product(
        article,
        name,
        price
    )



# Запись во вторую таблицу product_info
# article одинаковый в обеих таблицах
# для INNER JOIN
  
    await add_product_info(
        article,
        category,
        description
    )



    await message.answer(
        f"""
 Товар добавлен


 Артикул:
{article}


 Название:
{name}


 Цена:
{price} ₽


 Категория:
{category}


 Описание:
{description}
"""
    )



    # очищаем FSM

    await state.clear()
