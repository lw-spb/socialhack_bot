BOT_HTTP_API = '366866268:AAG0gu40s5nx2pOCKw_7wVOUO4kJOBhcef8'

options = [u'Расписание хакатона', u'Список экспертов', u'Задать вопрос организотору', ]
from telegram import InlineKeyboardButton
keyboard = [[InlineKeyboardButton(i, callback_data='%s'%i)] for i in options]
