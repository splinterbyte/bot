from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import States
from core.keyboards.reply import reply_keyboard

async def get_form(message: Message, state: FSMContext):
    await message.answer('Начинаем создание поста... Введите заголовок!')
    await state.set_state(States.GET_POSTNAME)

async def get_postname(message: Message, state: FSMContext):
    await message.answer('Теперь введи текст поста.')
    await state.update_data(name=message.text)
    await state.set_state(States.GET_TEXT)

async def get_text(message: Message, state: FSMContext):
    await message.answer('Теперь отправь фотографию!')
    await state.update_data(text=message.text)
    await state.set_state(States.GET_PHOTO)

async def get_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[0].file_id)
    data = await state.get_data()
    name = data.get("name")
    text = data.get("text")
    photo = data.get("photo")
    await message.answer(f'<u><b>Ваш пост готов!</b></u>\n\nПроверьте, верно ли введен заголовок: <u><b>{str.upper(name)}</b></u>\n\nА вот информация, которая появится на нем: \n\n', reply_markup=reply_keyboard)
    await message.answer_photo(photo, caption=text)
    await state.clear()
