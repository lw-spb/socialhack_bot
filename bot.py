from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import constants
from local import BOT_TOKEN_SECRET
from timing import timing
from experts import experts
from emoji import emojize
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class Bot:
    def __init__(self):
        self.updater = Updater(token=BOT_TOKEN_SECRET)
        self.dispatcher = self.updater.dispatcher

    def start(self, bot, update):
        reply_markup = InlineKeyboardMarkup(constants.keyboard)
        bot.sendMessage(chat_id=update.message.chat_id, text="Выбери опцию: ", reply_markup=reply_markup)


    def choose_option(self,  bot, update):
        query = update.callback_query
        option = query.data
        keyboard_back = [[InlineKeyboardButton(" <<< ", callback_data='back')]]
        reply_markup = InlineKeyboardMarkup(keyboard_back)

        if option.startswith('Расписание'):
            bot.sendMessage(chat_id=query.message.chat.id, text=timing, reply_markup=reply_markup)

        if option == 'back':
            text = 'Выбери опцию: '
            reply_markup = InlineKeyboardMarkup(constants.keyboard)
            bot.sendMessage(chat_id=query.message.chat.id, text=text, reply_markup=reply_markup)

        if option. startswith('Список'):
            bot.sendMessage(chat_id=query.message.chat.id, text=emojize(experts, use_aliases=True),
                            reply_markup=reply_markup)

        if option.startswith('Задать'):
            text = 'По всем вопросам пиши Дарье Локтевой: @Klimb или Лидии Ятлук: @lia_leonardi'
            bot.sendMessage(chat_id=query.message.chat.id, text=text, reply_markup=reply_markup)




if __name__ == '__main__':

    social_bot = Bot()

    start_handler = CommandHandler('start', social_bot.start)
    social_bot.dispatcher.add_handler(start_handler)

    social_bot.dispatcher.add_handler(CallbackQueryHandler(social_bot.choose_option))


    social_bot.updater.start_polling()
    social_bot.updater.idle()










