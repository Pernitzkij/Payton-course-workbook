import webbrowser
import telebot
from telebot import types
import sqlite3
# код для SQL запросов и базы данных
bot = telebot.TeleBot("6051421509:AAEzvSvTQIj1F0tmr6Q2paVwUK50Gr7Iqkc", parse_mode=None)
name = None

@bot.message_handler(commands=['start'])
def start(message):
	conn = sqlite3.connect('telegram.sql')
	cur= conn.cursor()

	cur.execute('CREATE TABLE IF NOT EXISTS users '
				'(id int auto_increment primary key, '
				'name varchar(50), pass varchar(50))')

	conn.commit()
	cur.close()
	conn.close()

	bot.send_message(message.chat.id, 'Регистрация, укажите имя ')
	bot.register_next_step_handler(message,user_name)

def user_name(message):
	global name
	name = message.text.strip()
	bot.send_message(message.chat.id, 'Введите пароль')
	bot.register_next_step_handler(message,user_pass)


def user_pass(message):
	password = message.text.strip()

	conn = sqlite3.connect('telegram.sql')
	cur = conn.cursor()

	cur.execute("INSERT INTO users (name,pass) VALUES ('%s','%s')" % (name,password))

	conn.commit()
	cur.close()
	conn.close()


	marcap = telebot.types.InlineKeyboardMarkup()
	marcap.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
	bot.send_message(message.chat.id, 'пользователь зарегистрирован', reply_markup=marcap)



@bot.callback_query_handler(func=lambda call: True)
def callback(call):
	conn = sqlite3.connect('telegram.sql')
	cur = conn.cursor()

	cur.execute('SELECT * FROM users')
	users=cur.fetchall()
	info=''
	for i in users:
		info += f'Имя: {i[1]}, пароль: {i[2]}\n '
	cur.close()
	conn.close()
	bot.send_message(call.message.chat.id, info)




bot.polling(none_stop=True)




