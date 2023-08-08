from aiogram import Bot, types, F
from aiogram.types import Message
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def get_start(message: Message, bot: Bot):
    await message.answer(f'Приветствую тебя, <b>{message.from_user.first_name}</b>.\n\nБлагодаря Конструктору вы можете создавать посты на своем сайте.\n\nНажмите на кнопку <b>меню</b>, чтобы увидеть список команд.')


async def descr_command(message: Message, bot: Bot):
    await message.answer('Конструктор - text') 


async def open_constructor(message: Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Открыть конструктор", web_app=WebAppInfo(url='http://45.153.70.246:80/')
        )
    )
    await message.answer(
        'Для перехода в Конструктор нажми на кнопку!',
        reply_markup=builder.as_markup(),
    )
   