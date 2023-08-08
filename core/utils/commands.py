from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Начало работы'),
        BotCommand(command='your_site', description='Твой сайт'),
        BotCommand(command='description', description='Описание бота')
        # BotCommand(command='new_post', description='Создать новый пост')
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
