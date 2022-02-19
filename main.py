import telebot
from telebot import types

token = "2091503539:AAFqFG58zyRmBLXOLVvgcUGCcpANs1kUSoU"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/start", "Хочу", "/help", "/rating", "Расписание", "Пока")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['rating'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/start", "Хочу", "/help", "/rating", "Расписание", "Пока")
    bot.send_message(message.chat.id, 'Тогда тебе сюда - http://room.mtuci.ru', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею выполнять такие команды как')
    bot.send_message(message.chat.id, '/start /help /rating Пока Хочу Расписание ')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/')
    elif message.text.lower() == "пока":
        bot.send_message(message.chat.id, 'Всего хорошего, друг')
    elif message.text.lower() == 'расписание':
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/time-table/')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'расписание':
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/time-table/')

bot.infinity_polling()