from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery, Message

router = Router()


class Form(StatesGroup):
    admin_answer = State()


@router.callback_query(F.data == "answer")
async def answer(callback: CallbackQuery, state: FSMContext):
    await state.set_state(state=Form.admin_answer)
    await callback.answer("")
    text = callback.message.text
    for i in text.split():
        if "id:" in i:
            text = i[3:]
            break
    await callback.message.answer(text="Введите ответ")
    await state.update_data(id=text)


@router.message(Form.admin_answer)
async def admin(message: Message, state: FSMContext):
    data = await state.get_data()
    print(data["id"])
    print(message.text)
    await message.send_copy(chat_id=data["id"])
    await state.clear()
