from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

remove_kb = ReplyKeyboardRemove()

answer_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Ответить", callback_data="answer")]
]
)
