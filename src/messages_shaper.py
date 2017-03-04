#!/usr/bin/env python3
# coding=utf-8


#DATA BLOCK
###############################################################


#EMOJIES
TORNADO = u'\U0001F32A'
THUNDERSTORM  = u'\U000026C8'
SUN = u'\U0001F323'
RAIN = u'\U0001F327'
SNOW = u'\U0001F328'
SUN_BEHIND_CLOUD = u'\U000026C5'
WHITE_SUN_WITH_SMALL_CLOUD = u'\U0001F324'
WHITE_SUN_BEHIND_CLOUD_WITH_RAIN = u'\U0001F326'
WIND = u'\U0001F32C'
FOG = u'\U0001F32B'
CLOUD = u'\U00002601'
FROST = u'\U00002744'
DRIZZLE = u'\U0001F4A7'
SNOWMAN = u'\U00002603'
CALENDAR = u'\U0001F4C5'
UNDEFINED = u'\U0000003F'
THERMOMETER = u'\U0001F321'

#################################################################

"""
All codes can be seen here : https://developer.yahoo.com/weather/documentation.html
"""
def get_weather_emoji(code=3200):
    if code in [0, 1, 2]:
        return TORNADO
    elif code in [3, 4, 17, 35, 37, 38, 39, 40]:
        return THUNDERSTORM
    elif code == 9:
        return DRIZZLE
    elif code in [5, 6, 7, 8, 10, 18]:
        return RAIN + SNOW
    elif code in [11, 12]:
        return RAIN
    elif code in [13, 14, 15, 16]:
        return SNOW + WIND
    elif code in [19, 20, 21, 22]:
        return FOG
    elif code == 24:
        return WIND
    elif code == 25:
        return FROST
    elif code in [26, 27, 28, 29, 30]:
        return SUN_BEHIND_CLOUD
    elif code in [31, 32, 33, 34, 36]:
        return CLEAR
    elif code in [41, 42, 43, 44, 45, 46]:
        return SNOW + SNOWMAN + SNOW
    else:
        return UNDEFINED


def shape_simple_message(data):
    useful_data = data['item']['forecast']

    # append plus, if number is positive
    if useful_data['low'][0].isdigit():
        useful_data['low'] = "+" + useful_data['low']
    if useful_data['high'][0].isdigit():
        useful_data['high'] = "+" + useful_data['high']

    formed_data = ("{date_symbol} Date: {date}\n {celsius_symbol} Temperature: {temperature}\n"
     "{condition_symbol} Condition: {condition}\n") \
     .format(date_symbol=CALENDAR, date=useful_data['date'], celsius_symbol=THERMOMETER, \
     temperature=useful_data['low'] + " --- " + useful_data['high'], \
     condition_symbol=get_weather_emoji(int(useful_data['code'])), \
     condition=useful_data['text'])

    return formed_data
