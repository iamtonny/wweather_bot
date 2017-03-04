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
#
# @bot.message_handler(commands=['weather'])
# def weather_city(message):
#     print(message['text'])
#     bot.reply_to(message, 'Hello, ' + message.from_user.first_name)
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


import telebot
from flask import Flask
from telebot import util
from queryes import get_weather

import config
import messages_shaper
from database import db_session
from database import init_db
from models import User

bot = telebot.TeleBot(config.token)
app = Flask(__name__)

@bot.message_handler(commands=['weather'])
def weather_city(message):
    city = ' '.join(message.text.split(' ')[1:])
    user = User.query.filter_by(id=message.from_user.id).first()

    if user is None:
        user = User(user_id=message.from_user.id, username=message.from_user.username, city=city)
        db_session.add(user)
        db_session.commit()
    else:
        pass

    mode_simple = False

    ten_days_weather_raw = get_weather(city, mode_simple)

    if ten_days_weather_raw is not None:
        if not mode_simple:
            # complex information are the same in each of days
            complex_messages = messages_shaper.shape_complex_weather_message(ten_days_weather_raw[0])

            for msg in complex_messages:
                bot.send_message(message.chat.id, msg)

        for day_weather_raw in ten_days_weather_raw:
            bot.send_message(message.chat.id, messages_shaper.shape_simple_weather_message(day_weather_raw['item']['forecast']))
    else:
        bot.send_message(message.chat.id, messages_shaper.MESSAGE_CITY_NOT_FOUND)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Flask will automatically remove database sessions
    at the end of the request or when the application shuts down.
    """
    db_session.remove()


if __name__ == '__main__':
    init_db()
    bot.polling(none_stop=True)
