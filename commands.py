from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram import Router

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(text="Привет!\nЭто бот обратной связи.\nВы можете написать и вам ответят(может быть).")
