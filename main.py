import os
import logging
from tmdb.application.MovieInfoGetter import MovieInfoGetter
from telegrambot.application.MovieMessageFormatter import MovieMessageFormatter

from telegram import Update
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackContext, MessageHandler, Filters

GET_MOVIE_INFORMATION = range(1)

def main() -> None:
    logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger = logging.getLogger()

    updater = Updater(os.getenv("TELEGRAM_BOT_KEY"))
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('find_by_id', find_by_id)],
        states={
            GET_MOVIE_INFORMATION : [MessageHandler(Filters.text & ~Filters.command, get_movie_information)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

def find_by_id(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Dame el id de la película:")
    return GET_MOVIE_INFORMATION

def get_movie_information(update: Update, context: CallbackContext):
    movie_id = update.message.text
    movie = MovieInfoGetter.get_movie_by_id(movie_id)
    message = MovieMessageFormatter(movie).format()
    update.message.reply_photo(movie.backdrop_url, caption=message, parse_mode="HTML")

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Bye! I hope we can talk again some day.')
    return ConversationHandler.END

if __name__=="__main__":
    main()
