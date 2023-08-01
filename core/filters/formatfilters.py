from aiogram.types import Message

async def check_photo(message: Message):
        await message.reply('Это не фото!')