import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater(os.getenv("TELEGRAM_BOT_KEY"))

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()