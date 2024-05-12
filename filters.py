from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram import Router, F, Bot
from keyboards import answer_kb
from config import ADMIN

router = Router()


@router.message(F.text)
async def text_filter(message: Message, bot: Bot):
    await bot.send_message(text=f"От пользователя @{message.from_user.username}\nid:{message.from_user.id}\n пришло новое сообщение:\n\n<blockquote>{message.text}</blockquote>", chat_id=ADMIN, parse_mode="html", reply_markup=answer_kb)


@router.message(F.photo)
async def photo_filter(message: Message, bot: Bot):
    await bot.send_photo(photo=message.photo[-1].file_id, caption=f"От пользователя @{message.from_user.username}\nid:{message.from_user.id}\n пришло новое фото", chat_id=ADMIN, reply_markup=answer_kb)


@router.message(F.video)
async def video_filter(message: Message, bot: Bot):
    await bot.send_video(video=message.video.file_id, caption=f"От пользователя @{message.from_user.username}\nid:{message.from_user.id}\n пришло новое видео", chat_id=ADMIN, reply_markup=answer_kb)


@router.message(F.document)
async def document_filter(message: Message, bot: Bot):
    await bot.send_document(document=message.document.file_id, caption=f"От пользователя @{message.from_user.username}\nid:{message.from_user.id}\n пришло новый файл", chat_id=ADMIN, reply_markup=answer_kb)


@router.message(F.audio)
async def audio_filter(message: Message, bot: Bot):
    await bot.send_audio(audio=message.audio.file_id, caption=f"От пользователя @{message.from_user.username}\nid:{message.from_user.id}\n пришло новое аудио", chat_id=ADMIN, reply_markup=answer_kb)


@router.message(F.voice)
async def voice_filter(message: Message, bot: Bot):
    await bot.send_voice(voice=message.voice.file_id, caption=f"От пользователя @{message.from_user.username}\nid:{message.from_user.id}\n пришло новое голосовое сообщение", chat_id=ADMIN, reply_markup=answer_kb)


@router.message(F.sticker)
async def sticker_filter(message: Message, bot: Bot):
    await bot.send_sticker(sticker=message.sticker.file_id, chat_id=ADMIN)
    await bot.send_message(text=f"От пользователя @{message.from_user.username}\nid:{message.from_user.id}\n пришел новый стикер⬆⬆⬆", chat_id=ADMIN, reply_markup=answer_kb)
