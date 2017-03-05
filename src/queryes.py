#!/usr/bin/env python3
# coding=utf-8

import urllib.parse
import urllib.request
import json
import eventlet
from urllib.error import HTTPError

import config


def get_weather(city=None, details=False):
    """Obtaining weather
    with a query to the config.BASE_URL.
    Return raw json data.
    """

    if not details:
        yql_query = ("select item.forecast from weather.forecast "
                     "where woeid in (select woeid from geo.places(1) where text=\"" + city + "\") and u=\"c\"")
    else:
        yql_query = ("select wind, atmosphere, astronomy, item.forecast from weather.forecast "
                     "where woeid in (select woeid from geo.places(1) where text=\"" + city + "\") and u=\"c\"")

    yql_url = config.BASE_QUERY_URL + \
        urllib.parse.urlencode({'q': yql_query}) + "&format=json"

    # Set timeout for set time limit query.
    timeout = eventlet.Timeout(10)

    # For invalid requests
    try:
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result.decode("utf-8"))
    except (HTTPError, eventlet.timeout.Timeout) as e:
        data = None
    finally:
        timeout.cancel()

    if data is None or data['query'] is None or data['query']['results'] is None or \
            data['query']['results']['channel'] is None:
        return None

    return data['query']['results']['channel']


if __name__ == "__main__":
    print(get_weather('minsk'))
