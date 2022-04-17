import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def search_movie(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Tell me the movie name')
    return 1

def list_movies(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'This should call API with {update.message.text}')

def close(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']

    update.message.reply_text(
        f"Restarting conversation"
    )

    user_data.clear()
    return ConversationHandler.END

updater = Updater(os.getenv("TELEGRAM_BOT_KEY"))

updater.dispatcher.add_handler(CommandHandler('hello', hello))

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('search_movie', search_movie)],
    states={
        1: [MessageHandler(Filters.text, list_movies)],
    },
    fallbacks=[CommandHandler('close', close)],
)
updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()