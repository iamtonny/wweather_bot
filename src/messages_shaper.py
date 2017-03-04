#!/usr/bin/env python3
# coding=utf-8


# DATA BLOCK
###############################################################


# EMOJIES
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
CELSIUS = u'\U00002103'
PENSIVE_FACE = u'\U0001F614'
DIRECTION = u'\U000027B7'
ATMOSPHERE = u'\U0001F301'
VISIBILITY = u'\U0001F453'
PRESSURE = u'\U0001F635'
ASTRONOMY = u'\U00002609'
SUNRISE = u'\U0001F305'
SUNSET = u'\U0001F307'

# MESSAGES
MESSAGE_CITY_NOT_FOUND = "Sorry, but city is not found." + PENSIVE_FACE

#################################################################

def get_weather_emoji(code=3200):
    """Return emoji by code.
    All codes can be seen here : https://developer.yahoo.com/weather/documentation.html
    """
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
        return SUN
    elif code in [41, 42, 43, 44, 45, 46]:
        return SNOW + SNOWMAN + SNOW
    else:
        return UNDEFINED


def shape_simple_weather_message(data):
    """Generate a simple message types.
    Return formed message.
    """

    useful_data = data['item']['forecast']

    formed_data = ("{date_symbol} Date: {date}\n"
     "{termometer_symbol} Temperature: {temperature}\n"
     "{condition_symbol} Condition: {condition}\n") \
     .format(date_symbol=CALENDAR, date=useful_data['date'], termometer_symbol=THERMOMETER, \
     temperature=useful_data['low'] + CELSIUS + " --- " + useful_data['high'] + CELSIUS, \
     condition_symbol=get_weather_emoji(int(useful_data['code'])), \
     condition=useful_data['text'])

    return formed_data


def shape_complex_weather_message(data):
    """Generate a complex message types.
    Return set of formed messages.
    """

    formed_wind_data = ("      {wind_symbol} Wind:\n"
     "{wind_temperature_symbol} Chill: {chill}\n"
     "{direction_symbol} Direction: {direction}\n"
     "{speed_symbol} Speed: {speed}\n") \
     .format(wind_symbol=WIND, wind_temperature_symbol = THERMOMETER, chill = data['wind']['chill'], \
     direction_symbol=DIRECTION, direction=data['wind']['direction'], speed_symbol=FOG, \
     speed = data['wind']['speed'])

    formed_atmosphere_data = ("      {atmosphere_symbol} Atmosphere:\n"
     "{humidity_symbol} Humidity: {humidity}\n"
     "{visibility_symbol} Visibility: {visibility}\n"
     "{pressure_symbol} Pressure: {pressure}\n") \
     .format(atmosphere_symbol=ATMOSPHERE, humidity_symbol = DRIZZLE, humidity = data['atmosphere']['humidity'] + '%', \
     visibility_symbol=VISIBILITY, visibility=data['atmosphere']['visibility'], pressure_symbol=PRESSURE, \
     pressure = data['atmosphere']['pressure'])

    formed_astronomy_data = ("      {astronomy_symbol} Astronomy:\n"
     "{sunrise_symbol} Sunrise: {sunrise}\n"
     "{sunset_symbol} Sunset: {sunset}\n") \
     .format(astronomy_symbol=ASTRONOMY, sunrise_symbol=SUNRISE, sunrise=data['astronomy']['sunrise'], \
     sunset_symbol=SUNSET, sunset=data['astronomy']['sunset'])

    formed_data = [formed_wind_data, formed_atmosphere_data, formed_astronomy_data]

    return formed_data
