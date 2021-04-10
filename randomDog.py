from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

load_dotenv()


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def dog(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    url = get_url()
    context.bot.send_photo(chat_id=chat_id, photo=url)


if __name__ == '__main__':
    updater = Updater(os.getenv('API_KEY'))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dog', dog))
    updater.start_polling()
    updater.idle()
