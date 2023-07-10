import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot("6051421509:AAEzvSvTQIj1F0tmr6Q2paVwUK50Gr7Iqkc")
currency = CurrencyConverter()
amout = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Введите сумму: ')
    bot.register_next_step_handler(message,summa)


def summa(message):
    global amout
    try:
        amout = int( message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Не верный формат')
        bot.register_next_step_handler(message,summa)
        return
    if amout > 0:
        makup = types.InlineKeyboardMarkup(row_width=2)

        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('друге значение', callback_data='else')
        makup.add(btn4,btn3,btn1,btn2)
        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=makup)
    else:
        bot.send_message(message.chat.id, 'Очень маленькое число')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res=currency.convert(amout, values[0],values[1])
        bot.send_message(call.message.chat.id, f'Получается: {round(res,2)}. Можете заново вписать сумму')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Введите парук через "/"')
        bot.register_next_step_handler(call.message, my_currency)

def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amout, values[0], values[1])
        bot.send_message(message.chat.id, f'Получается: {round(res, 2)}. Можете заново вписать сумму')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, f'Что то нек так. Впишите значение снова')
        bot.register_next_step_handler(message, my_currency)






bot.polling(none_stop=True)