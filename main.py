import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from database.main_db import create_table

from handlers.fsm import router



async def main():

    bot = Bot(
        token=BOT_TOKEN
    )


    dp = Dispatcher()


    dp.include_router(router)


    # создаём таблицы
    await create_table()


    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())
