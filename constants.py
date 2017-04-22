options = [u'Расписание хакатона', u'Список экспертов', u'Задать вопрос организатору', ]
from telegram import InlineKeyboardButton
keyboard = [[InlineKeyboardButton(i, callback_data='%s'%i)] for i in options]
