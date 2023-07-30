from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from core.handlers.basic import *
from core.settings import settings
from aiogram.filters import Command
from core.utils.commands import set_commands
from core.handlers import form
from core.utils.statesform import States
from core.filters import formatfilters 



import asyncio
import logging

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='BOT IS RUNNING')
    

async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    
    
    dp.startup.register(start_bot)
    
    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(descr_command, Command(commands='description'))
    dp.message.register(your_site, Command(commands='your_site'))
    dp.message.register(form.get_form, Command(commands='new_post'))
    dp.message.register(form.get_form, F.text == 'Создать новый пост')


    dp.message.register(form.get_postname, States.GET_POSTNAME)
    dp.message.register(form.get_text, States.GET_TEXT)
    dp.message.register(formatfilters.check_photo, lambda message: not message.photo)
    dp.message.register(form.get_photo, States.GET_PHOTO)
    
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())