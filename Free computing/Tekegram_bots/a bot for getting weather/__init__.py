
import telebot
import requests

import json

bot = telebot.TeleBot("6051421509:AAEzvSvTQIj1F0tmr6Q2paVwUK50Gr7Iqkc")
API = 'ba48b32d38f61b6d842bab6c443de443'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Напишите название города: ')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:

        data = json.loads(res.text)

        bot.reply_to(message, f"Сейчас погода: {round(data['main']['temp'])} градусов")
    else:
        bot.reply_to(message, f"Город указан не верно: '{city}'")


bot.polling(none_stop=True)
