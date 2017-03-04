#!/usr/bin/env python3
# coding=utf-8


# import os
# import json
#
# import telebot
# from flask import Flask, request
# from queryes import get_weather
#
# import config
#
#
# bot = telebot.TeleBot(config.token)
# app = Flask(__name__)
#
# """
# Handler on "start" command
# """
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.reply_to(message, 'Hello, ' + message.from_user.first_name)
#
# @bot.message_handler(commands=['weather'])
# def weather_city(message):
#     print(message['text'])
#     bot.reply_to(message, 'Hello, ' + message.from_user.first_name)
#
# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def echo_message(message):
#     bot.reply_to(message, message.text)
#
# @app.route("/bot", methods=['POST'])
# def getMessage():
#     bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#     return "!", 200
#
# @app.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url="https://shielded-lowlands-74701.herokuapp.com/bot")
#     return "!", 200
#
# app.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
# app = Flask(__name__)


import config
import telebot
from telebot import util
from queryes import get_weather
from messages_shaper import shape_simple_message

bot = telebot.TeleBot(config.token)

# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
#     bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=['weather'])
def weather_city(message):
    city = ' '.join(message.text.split(' ')[1:])
    ten_days_weather = get_weather(city, simple=True)
    for day_weather in ten_days_weather:
        bot.send_message(message.chat.id, shape_simple_message(day_weather))


if __name__ == '__main__':
     bot.polling(none_stop=True)
