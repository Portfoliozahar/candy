from aiogram import types
from create_bot import bot


async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, f'Здарова {message.from_user.first_name}!\n'
                                                 f'Давай сыграем у кого первее диабет!')
