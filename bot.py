import asyncio
import logging
import re

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from config import bot_api_key
from text_utils import compile_mil_massage


logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_api_key)
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    print(message.chat.id)
    await message.answer(f'Hello, {message.chat.username}!\n'
                         f'Enter message to convert it to ICAO: ')


@dp.message()
async def militarize_message(message: types.Message):
    if re.search(r'[А-я]+', message.text):
        result_message = await compile_mil_massage(message_text=message.text,
                                                   lang_mode='ru')
    else:
        result_message = await compile_mil_massage(message_text=message.text,
                                                   lang_mode='en')

    await message.reply(result_message)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
