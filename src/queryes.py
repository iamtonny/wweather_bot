#!/usr/bin/env python3
# coding=utf-8


def get_weather(city):
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = "select location, wind, atmosphere, astronomy, item.forecast\
     from weather.forecast where woeid in (select woeid from geo.places(1) where text=" + city+ ") and u=\"c\""
    yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
    result = urllib.request.urlopen(yql_url).read()
    data = json.loads(result.decode("utf-8"))
    return data['query']['results']
