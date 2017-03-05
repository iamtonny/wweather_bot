#!/usr/bin/env python3
# coding=utf-8

import constants


def get_weather_emoji(code=3200):
    """Return emoji by code.
    All codes can be seen here : https://developer.yahoo.com/weather/documentation.html
    """
    if code in [0, 1, 2]:
        return constants.EMOJI_TORNADO
    elif code in [3, 4, 17, 35, 37, 38, 39, 40]:
        return constants.EMOJI_THUNDERSTORM
    elif code == 9:
        return constants.EMOJI_DRIZZLE
    elif code in [5, 6, 7, 8, 10, 18]:
        return constants.EMOJI_RAIN + constants.EMOJI_SNOW
    elif code in [11, 12]:
        return constants.EMOJI_RAIN
    elif code in [13, 14, 15, 16]:
        return constants.EMOJI_SNOW + constants.EMOJI_WIND
    elif code in [19, 20, 21, 22]:
        return constants.EMOJI_FOG
    elif code == 24:
        return constants.EMOJI_WIND
    elif code == 25:
        return constants.EMOJI_FROST
    elif code in [26, 27, 28, 29, 30]:
        return constants.EMOJI_SUN_BEHIND_CLOUD
    elif code in [31, 32, 33, 34, 36]:
        return constants.EMOJI_SUN
    elif code in [41, 42, 43, 44, 45, 46]:
        return constants.EMOJI_SNOW + constants.EMOJI_SNOWMAN + constants.EMOJI_SNOW
    else:
        return constants.EMOJI_UNDEFINED


def shape_simple_weather_message(data):
    """Generate a simple message types.
    Return formed message.
    """

    formed_data = ("{date_symbol} Date: {date}\n"
     "{termometer_symbol} Temperature: {temperature}\n"
     "{condition_symbol} Condition: {condition}\n") \
     .format(date_symbol=constants.EMOJI_CALENDAR, date=data['date'], termometer_symbol=constants.EMOJI_THERMOMETER, \
     temperature=data['low'] + constants.EMOJI_CELSIUS + " --- " + data['high'] + constants.EMOJI_CELSIUS, \
     condition_symbol=get_weather_emoji(int(data['code'])), \
     condition=data['text'])

    return formed_data


def shape_complex_weather_message(data):
    """Generate a complex message types.
    Return set of formed messages.
    """

    formed_wind_data = ("      {wind_symbol} Wind:\n"
     "{wind_temperature_symbol} Chill: {chill}\n"
     "{direction_symbol} Direction: {direction}\n"
     "{speed_symbol} Speed: {speed}\n") \
     .format(wind_symbol=constants.EMOJI_WIND, wind_temperature_symbol = constants.EMOJI_THERMOMETER, chill = data['wind']['chill'], \
     direction_symbol=constants.EMOJI_DIRECTION, direction=data['wind']['direction'], speed_symbol=constants.EMOJI_FOG, \
     speed = data['wind']['speed'])

    formed_atmosphere_data = ("      {atmosphere_symbol} Atmosphere:\n"
     "{humidity_symbol} Humidity: {humidity}\n"
     "{visibility_symbol} Visibility: {visibility}\n"
     "{pressure_symbol} Pressure: {pressure}\n") \
     .format(atmosphere_symbol=constants.EMOJI_ATMOSPHERE, humidity_symbol = constants.EMOJI_DRIZZLE, humidity = data['atmosphere']['humidity'] + '%', \
     visibility_symbol=constants.EMOJI_VISIBILITY, visibility=data['atmosphere']['visibility'], pressure_symbol=constants.EMOJI_PRESSURE, \
     pressure = data['atmosphere']['pressure'])

    formed_astronomy_data = ("      {astronomy_symbol} Astronomy:\n"
     "{sunrise_symbol} Sunrise: {sunrise}\n"
     "{sunset_symbol} Sunset: {sunset}\n") \
     .format(astronomy_symbol=constants.EMOJI_ASTRONOMY, sunrise_symbol=constants.EMOJI_SUNRISE, sunrise=data['astronomy']['sunrise'], \
     sunset_symbol=constants.EMOJI_SUNSET, sunset=data['astronomy']['sunset'])

    formed_data = [formed_wind_data, formed_atmosphere_data, formed_astronomy_data]

    return formed_data
