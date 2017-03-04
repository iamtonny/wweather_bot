#!/usr/bin/env python3
# coding=utf-8
import urllib.parse
import urllib.request
import json


def get_weather(city, simple=True):
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    if simple:
        yql_query = ("select item.forecast from weather.forecast "
            "where woeid in (select woeid from geo.places(1) where text=\"" + city + "\") and u=\"c\"")
    else:
        yql_query = ("select location, wind, atmosphere, astronomy, item.forecast from weather.forecast "
            "where woeid in (select woeid from geo.places(1) where text=\"" + city + "\") and u=\"c\"")
    yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
    result = urllib.request.urlopen(yql_url).read()
    data = json.loads(result.decode("utf-8"))
    return data['query']['results']['channel']


if __name__ == "__main__":
    print(get_weather('minsk'))
