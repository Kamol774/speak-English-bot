"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from aiogram import Bot, Dispatcher, executor, types

from oxfordLookup import getDefinitions
from googletrans import Translator
from settings import local_settings

translator = Translator()

API_TOKEN = local_settings.TELEGRAM_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm Poliglot!  \n You can write any word or text in order to get definitions or to translate")


@dp.message_handler()
async def tarjimon(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang=='en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup = getDefinitions(word_id)
        if lookup:
            await message.reply(f"word: 👆🏻 \nDefinitions: \n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so'z mavjud emas")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)