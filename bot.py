#!/usr/bin/env python3
# coding=utf-8

import os
import telebot
from flask import Flask
from flask import request

import src.config as config
import src.messages_shaper as messages_shaper
import src.constants as constants
import src.inspection as inspection
from src.database import db_session
from src.database import init_db
from src.models import User
from src.queryes import get_weather


bot = telebot.TeleBot(config.TOKEN)
app = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    user = User.query.filter_by(telegram_id=message.from_user.id).first()

    if user is None:
        user = User(
            telegram_id=message.from_user.id,
            username=message.from_user.username)
        db_session.add(user)
        db_session.commit()

    bot.send_message(message.chat.id, constants.MESSAGE_HELLO)


@bot.message_handler(commands=['settings', 'help'])
def settings(message):

    user = User.query.filter_by(telegram_id=message.from_user.id).first()

    bot.send_message(message.chat.id, constants.MESSAGE_SETTINGS)

    if user is not None:
        city = constants.MESSAGE_UNDERFINED if user.city is None else user.city
        bot.send_message(
            message.chat.id,
            constants.MESSAGE_CURRENT_CITY +
            city)

    bot.send_message(message.chat.id, constants.MESSAGE_COMMANDS)


@bot.message_handler(commands=['sethome'])
def set_home(message):

    user = User.query.filter_by(telegram_id=message.from_user.id).first()
    city = ' '.join(message.text.split(' ')[1:])

    if user is not None and city is not None:
        user.city = city
        db_session.commit()
        bot.send_message(
            message.chat.id,
            constants.MESSAGE_CITY_WAS_SET +
            city)
    else:
        bot.send_message(message.chat.id, constants.MESSAGE_WRONG)


@bot.message_handler(commands=['hidedetails'])
def hide_details(message):

    user = User.query.filter_by(telegram_id=message.from_user.id).first()

    if user is not None:
        user.details = False
        db_session.commit()
        bot.send_message(message.chat.id, constants.MESSAGE_DETAILS_HIDDEN)
    else:
        bot.send_message(message.chat.id, constants.MESSAGE_WRONG)


@bot.message_handler(commands=['showdetails'])
def show_details(message):

    user = User.query.filter_by(telegram_id=message.from_user.id).first()

    if user is not None:
        user.details = True
        db_session.commit()
        bot.send_message(message.chat.id, constants.MESSAGE_DETAILS_VISIBLE)
    else:
        bot.send_message(message.chat.id, constants.MESSAGE_WRONG)


@bot.message_handler(commands=['setdays'])
def set_days(message):

    days = ' '.join(message.text.split(' ')[1:])
    user = User.query.filter_by(telegram_id=message.from_user.id).first()

    if user is not None and inspection.represent_int(days):
        user.num_display_days = int(days)
        db_session.commit()
        bot.send_message(
            message.chat.id,
            constants.MESSAGE_SET_DAYS +
            str(days))
    else:
        bot.send_message(message.chat.id, constants.MESSAGE_WRONG)


@bot.message_handler(commands=['weather'])
def weather_city(message):

    city = ' '.join(message.text.split(' ')[1:])
    user = User.query.filter_by(telegram_id=message.from_user.id).first()

    if user is None:
        return
    elif user is not None and not city:
        city_for_find = ""

        if user.city is not None:
            city_for_find = user.city

        all_days_weather_raw = get_weather(
            city=city_for_find, details=user.details)

    elif user is not None and city:
        all_days_weather_raw = get_weather(city=city, details=user.details)

    if all_days_weather_raw is not None:

        if user.details:
            # complex information are the same in each of days
            complex_messages = messages_shaper.shape_complex_weather_message(
                all_days_weather_raw[0])

            for msg in complex_messages:
                bot.send_message(message.chat.id, msg)

        for day_weather_raw in all_days_weather_raw[:user.num_display_days]:
            bot.send_message(
                message.chat.id,
                messages_shaper.shape_simple_weather_message(
                    day_weather_raw['item']['forecast']))
    else:
        bot.send_message(message.chat.id, constants.MESSAGE_CITY_NOT_FOUND)


@app.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://shielded-lowlands-74701.herokuapp.com/bot")
    return "!", 200


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Flask will automatically remove database sessions
    at the end of the request or when the application shuts down.
    """
    db_session.remove()


init_db()
app.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
app = Flask(__name__)
