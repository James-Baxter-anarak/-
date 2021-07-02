# import glob
# import random
# import random

import telebot
from telebot import types

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def send_welcomm(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton('Случайные фотографии', callback_data='first')
    markup.add(btn1)
    send_mess = f'<b>Привет {message.from_user.first_name}</b>!\nЯ могу отправить ' \
                f'интересные фотографии =)'
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: 'first' in call.data)
def answer(call):
    if call.data == 'first':
        pictures = open('D:\gay4.png', 'rb')
        bot.send_photo(call.message.chat.id, pictures)


@bot.message_handler(commands=['vk'])
def open_vk(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить VK разработчика', url='https://vk.com/eerlish'))
    bot.send_message(message.chat.id,
                     'To visit the developer page just click on the button:',
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['help'])
def comm_help(message):
    bot.send_message(message.chat.id,
'''Anarak - бот на стадии разработки. Вы имеете доступ к некоторым командам:
\n/help - выводит доступные команды
\n/start - предлагает фото
\n/vk - отправляет ссылку на разработчика(vk)'''
)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.strip().title() == 'Привет':
        bot.send_message(message.chat.id, 'Привет гавно')


@bot.message_handler(content_types=['photo'])
def send_pict(message):
    photo = open('D:\gay4.png', 'rb')
    if message.text.strip().title() == 'Пр':
        bot.send_photo(message.chat.id, photo)


bot.polling()
