import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWords

API_TOKEN = '6110446453:AAELjpWZ15Uj5ipiv5H9lZmWSNf0wnqeQ30'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("""Assalomu alaykum. "UzImlo" botiga xush kelibsiz""")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Dasturchi: @MrZafarov")


@dp.message_handler()
async def checkImlo(message: types.Message):
    words = message.text.split()
    for word in words:
        result = checkWords(word)
        if result['available']:
            response = f"✅ {word.capitalize()}"
        else:
            response = f"❌ {word.capitalize()}\n"
            for text in result['matches']:
                response += f"✅ {text.capitalize()}\n"
        await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)