from aiogram import Bot, types, F
from aiogram.types import Message
# from core.keyboards.reply import reply_keyboard
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def get_start(message: Message, bot: Bot):
    await message.answer(f'Приветствую Вас, <b>{message.from_user.first_name}</b>.\n\nБлагодаря этому боту вы можете создавать посты на своем сайте.\n\nНажмите на кнопку <b>меню</b>, чтобы увидеть список команд.')


async def descr_command(message: Message, bot: Bot):
    await message.answer('Благодаря этому боту вы можете размещать на сайте посты, фотографии, менять темы и оформление.') 


async def your_site(message: Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Launch app", web_app=WebAppInfo(url='http://45.153.70.246:3000/'))
    )
    await message.answer(
        'Launch app',
        reply_markup=builder.as_markup(),
    )
   