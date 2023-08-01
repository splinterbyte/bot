from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import States




async def check_photo(message: Message, state: FSMContext):
        await message.reply('Это не фото!')
