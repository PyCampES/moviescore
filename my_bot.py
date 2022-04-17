import os

from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext

import logging

import moviedb


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        f"Hello {update.effective_user.first_name}, echo {update.message.text}"
    )


def searchmovies(update: Update, context: CallbackContext) -> None:
    query = update.message.text.replace("/searchmovies ", "")
    movies = moviedb.search_movies(query)
    first_three_movies = [movie["original_title"] for movie in movies["results"][:3]]
    update.message.reply_text("; ".join(first_three_movies))


def render_movie_by_id(update: Update, context: CallbackContext) -> None:
    query = update.message.text.replace("/render_movie_by_id ", "")
    reply_message = moviedb.format_movie_by_id(query)
    logger.info(reply_message)
    update.message.reply_text(r    query = update.message.text.replace("/render_movie_by_id ", "")
    reply_message = moviedb.format_movie_by_id(query)
    logger.info(reply_message)eply_message)


updater = Updater(os.getenv("TELEGRAM_BOT_KEY"))

updater.dispatcher.add_handler(CommandHandler("hello", hello))
updater.dispatcher.add_handler(CommandHandler("searchmovies", searchmovies))
updater.dispatcher.add_handler(CommandHandler("render_movie_by_id", render_movie_by_id))

updater.start_polling()
updater.idle()
