import handlers

from create_bot import dp
from aiogram import executor

async def onStart(_):
    print('ssssssssssssssss')

handlers.registred_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=onStart) 