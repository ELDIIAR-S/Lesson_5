from aiogram import Router

from aiogram.filters import Command

from aiogram.types import Message


from database.main_db import get_products



router = Router()



@router.message(Command("products"))
async def show_products(
        message: Message
):


    products = await get_products()



    if not products:

        await message.answer(
            "Товаров нет"
        )

        return



    for product in products:


        article = product[0]

        name = product[1]

        price = product[2]

        category = product[3]

        description = product[4]



        text = f"""

  Товар

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


        await message.answer(text)