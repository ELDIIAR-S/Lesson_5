import asyncio

from aiogram import Bot, Dispatcher

from database.main_db import create_table

from handlers.fsm import router


from config import BOT_TOKEN



async def main():

    bot = Bot(
        token=BOT_TOKEN
    )


    dp = Dispatcher()


    dp.include_router(router)


    # создание таблиц при запуск
    create_table()


    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())