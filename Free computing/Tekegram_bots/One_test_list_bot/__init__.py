import webbrowser
import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot("6051421509:AAEzvSvTQIj1F0tmr6Q2paVwUK50Gr7Iqkc", parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
	conn = sqlite3.connect('telegram.sql')
	cur= conn.cursor()

	cur.execute('CREATE TABLE IN NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')

	conn.commit()
	cur.close()
	conn.close()

	bot.send_message(message.chat.id, 'Регистрация укажите имя ')
	bot.register_next_step_handler(message,user_name)

def user_name(message):
	pass


bot.polling(none_stop=True)

