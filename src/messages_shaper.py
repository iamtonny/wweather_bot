#!/usr/bin/env python3
# coding=utf-8


# DATA BLOCK
###############################################################


# EMOJIES
EMOJI_TORNADO = u'\U0001F32A'
EMOJI_THUNDERSTORM  = u'\U000026C8'
EMOJI_SUN = u'\U0001F323'
EMOJI_RAIN = u'\U0001F327'
EMOJI_SNOW = u'\U0001F328'
EMOJI_SUN_BEHIND_CLOUD = u'\U000026C5'
EMOJI_WHITE_SUN_WITH_SMALL_CLOUD = u'\U0001F324'
EMOJI_WHITE_SUN_BEHIND_CLOUD_WITH_RAIN = u'\U0001F326'
EMOJI_WIND = u'\U0001F32C'
EMOJI_FOG = u'\U0001F32B'
EMOJI_CLOUD = u'\U00002601'
EMOJI_FROST = u'\U00002744'
EMOJI_DRIZZLE = u'\U0001F4A7'
EMOJI_SNOWMAN = u'\U00002603'
EMOJI_CALENDAR = u'\U0001F4C5'
EMOJI_UNDEFINED = u'\U0000003F'
EMOJI_THERMOMETER = u'\U0001F321'
EMOJI_CELSIUS = u'\U00002103'
EMOJI_PENSIVE_FACE = u'\U0001F614'
EMOJI_DIRECTION = u'\U000027B7'
EMOJI_ATMOSPHERE = u'\U0001F301'
EMOJI_VISIBILITY = u'\U0001F453'
EMOJI_PRESSURE = u'\U0001F635'
EMOJI_ASTRONOMY = u'\U00002609'
EMOJI_SUNRISE = u'\U0001F305'
EMOJI_SUNSET = u'\U0001F307'

# MESSAGES
MESSAGE_CITY_NOT_FOUND = "Sorry, but city is not found." + EMOJI_PENSIVE_FACE

#################################################################

def get_weather_emoji(code=3200):
    """Return emoji by code.
    All codes can be seen here : https://developer.yahoo.com/weather/documentation.html
    """
    if code in [0, 1, 2]:
        return EMOJI_TORNADO
    elif code in [3, 4, 17, 35, 37, 38, 39, 40]:
        return EMOJI_THUNDERSTORM
    elif code == 9:
        return EMOJI_DRIZZLE
    elif code in [5, 6, 7, 8, 10, 18]:
        return EMOJI_RAIN + EMOJI_SNOW
    elif code in [11, 12]:
        return EMOJI_RAIN
    elif code in [13, 14, 15, 16]:
        return EMOJI_SNOW + EMOJI_WIND
    elif code in [19, 20, 21, 22]:
        return EMOJI_FOG
    elif code == 24:
        return EMOJI_WIND
    elif code == 25:
        return EMOJI_FROST
    elif code in [26, 27, 28, 29, 30]:
        return EMOJI_SUN_BEHIND_CLOUD
    elif code in [31, 32, 33, 34, 36]:
        return EMOJI_SUN
    elif code in [41, 42, 43, 44, 45, 46]:
        return EMOJI_SNOW + EMOJI_SNOWMAN + EMOJI_SNOW
    else:
        return EMOJI_UNDEFINED


def shape_simple_weather_message(data):
    """Generate a simple message types.
    Return formed message.
    """

    formed_data = ("{date_symbol} Date: {date}\n"
     "{termometer_symbol} Temperature: {temperature}\n"
     "{condition_symbol} Condition: {condition}\n") \
     .format(date_symbol=EMOJI_CALENDAR, date=data['date'], termometer_symbol=EMOJI_THERMOMETER, \
     temperature=data['low'] + EMOJI_CELSIUS + " --- " + data['high'] + EMOJI_CELSIUS, \
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
     .format(wind_symbol=EMOJI_WIND, wind_temperature_symbol = EMOJI_THERMOMETER, chill = data['wind']['chill'], \
     direction_symbol=EMOJI_DIRECTION, direction=data['wind']['direction'], speed_symbol=EMOJI_FOG, \
     speed = data['wind']['speed'])

    formed_atmosphere_data = ("      {atmosphere_symbol} Atmosphere:\n"
     "{humidity_symbol} Humidity: {humidity}\n"
     "{visibility_symbol} Visibility: {visibility}\n"
     "{pressure_symbol} Pressure: {pressure}\n") \
     .format(atmosphere_symbol=EMOJI_ATMOSPHERE, humidity_symbol = EMOJI_DRIZZLE, humidity = data['atmosphere']['humidity'] + '%', \
     visibility_symbol=EMOJI_VISIBILITY, visibility=data['atmosphere']['visibility'], pressure_symbol=EMOJI_PRESSURE, \
     pressure = data['atmosphere']['pressure'])

    formed_astronomy_data = ("      {astronomy_symbol} Astronomy:\n"
     "{sunrise_symbol} Sunrise: {sunrise}\n"
     "{sunset_symbol} Sunset: {sunset}\n") \
     .format(astronomy_symbol=EMOJI_ASTRONOMY, sunrise_symbol=EMOJI_SUNRISE, sunrise=data['astronomy']['sunrise'], \
     sunset_symbol=EMOJI_SUNSET, sunset=data['astronomy']['sunset'])

    formed_data = [formed_wind_data, formed_atmosphere_data, formed_astronomy_data]

    return formed_data
