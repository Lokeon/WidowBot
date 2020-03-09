import telegram
import random
import config
from telegram.ext import Updater, CommandHandler
from pathlib import Path


def ouihaw(bot, update):
    chat_id = update.message.chat_id
    pathX = Path(config.PATH)
    bot.send_photo(chat_id=chat_id, photo=open(
        random.choice(list(pathX.glob('*.jpg'))), 'rb'))


def mercymaker(bot, update):
    chat_id = update.message.chat_id
    pathX = Path(config.PATH)
    bot.send_photo(chat_id=chat_id, photo=open(
        random.choice(list(pathX.glob('*.jpg'))), 'rb'))


def main():
    updater = Updater(config.TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('ouihaw', ouihaw))
    dp.add_handler(CommandHandler('mercymaker', mercymaker))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
