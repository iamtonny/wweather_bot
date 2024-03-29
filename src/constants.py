#!/usr/bin/env python3
# coding=utf-8


# EMOJIES
EMOJI_TORNADO = u'\U0001F32A'
EMOJI_THUNDERSTORM = u'\U000026C8'
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
EMOJI_DETECTIVE = u'\U0001F575'
EMOJI_BACKHAND_RIGHT = u'\U0001F449'
EMOJI_CONSTRUCTION_WORKER = u'\U0001F477'
EMOJI_OLD_MAN = u'\U0001F474'
EMOJI_SETTINGS = u'\U00002699'
EMOJI_VULCAN_SALUTE = u'\U0001F596'
EMOJI_ROBOT_FACE = u'\U0001F916'

# MESSAGES
MESSAGE_CITY_NOT_FOUND = "Sorry, but city is not found." + EMOJI_PENSIVE_FACE
MESSAGE_CITY_WAS_SET = EMOJI_DETECTIVE + "City: "
MESSAGE_DETAILS_HIDDEN = EMOJI_BACKHAND_RIGHT + "Details hidden."
MESSAGE_DETAILS_VISIBLE = EMOJI_BACKHAND_RIGHT + "Details visible."
MESSAGE_SET_DAYS = EMOJI_CONSTRUCTION_WORKER + "Count of visible days: "
MESSAGE_WRONG = "Ooops... You have done something wrong" + EMOJI_OLD_MAN
MESSAGE_CURRENT_CITY = "Current city is: "
MESSAGE_UNDERFINED = "Underfined"
MESSAGE_COMMANDS = ("Commands:\n"
                    "/weather - get weather data for the saved city\n"
                    "/weather CITY - get weather data for the CITY\n"
                    "/sethome CITY- set the current CITY\n"
                    "/hidedetails - show only basic information\n"
                    "/showdetails - show all wheather information"
                    "/setdays DAYS - set the number of DAYS displayed. Max = 10\n")
MESSAGE_SETTINGS = EMOJI_SETTINGS + "Settings:\n "
MESSAGE_HELLO = ("{vulcan_salute}Hey, i'am weather bot {face} and i will find weather forecast to you my lord ;)\n"
                 "If you want to see my setting, please, enter \"/settings\" or \"/help\""
                 .format(vulcan_salute=EMOJI_VULCAN_SALUTE * 3, face=EMOJI_ROBOT_FACE))
