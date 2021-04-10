from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import pyshorteners

load_dotenv()


def shorten(update: Update, context: CallbackContext):
    text = update.message.text.split(" ")
    chat_id = update.message.chat.id

    if(len(text) == 1):
        context.bot.send_message(chat_id, "Insert at least one URL!")
    else:
        url = ""
        err = ""
        for x in text:
            if (not(x.startswith('/'))):
                if (x.startswith('http') or x.startswith('ftp')):
                    url = url + "\n" + pyshorteners.Shortener().tinyurl.short(x)
                else:
                    err = err + "\n" + x

        if url != "":
            context.bot.send_message(
                chat_id, f"✅ Shortened URL(s):\n{url}")
        if err != "":
            context.bot.send_message(chat_id, f"❌ Invalid(s) URL(s)!\n{err}")


if __name__ == '__main__':
    updater = Updater(os.getenv('BOT_API_KEY'))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('url', shorten, pass_args=True))
    updater.start_polling()
    updater.idle()
