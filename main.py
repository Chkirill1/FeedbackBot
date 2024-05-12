from aiogram import Bot, Dispatcher
from config import TOKEN
import asyncio
import logging
from commands import router
from filters import router as filter_router
from states import router as state_router


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    logging.basicConfig(level=logging.DEBUG)
    dp.include_routers(router, state_router, filter_router)
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
