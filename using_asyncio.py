"""
Babel is required.
"""

import logging

from aiogram import Bot, Dispatcher, executor, md, types
from tmdbv3api import TMDb
from tmdbv3api import Movie

API_TOKEN = "API_TOKEN"

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command.
    """
    await message.reply("Menu")


@dp.message_handler(commands=["search"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command.
    """
    await message.reply("Hi")
    movie_name = message["text"][8:]
    resp = await search(message)


# @dp.message_handler(commands=["search"])
async def search(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/hep` command.
    """
    tmdb = TMDb()
    tmdb.api_key = "YOUR_KEY"

    movie_name = message["text"][8:]
    movie = Movie()
    resp = movie.search(movie_name)
    logging.info(resp)
    await message.reply(md.text(md.bold("Info about your language:")))


@dp.message_handler()
async def check_language(message: types.Message):
    locale = message.from_user.locale

    await message.reply(
        md.text(
            md.bold("Info about your language:"),
            md.text("🔸", md.bold("Code:"), md.code(locale.language)),
            md.text("🔸", md.bold("Territory:"), md.code(locale.territory or "Unknown")),
            md.text("🔸", md.bold("Language name:"), md.code(locale.language_name)),
            md.text(
                "🔸", md.bold("English language name:"), md.code(locale.english_name)
            ),
            sep="\n",
        )
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
