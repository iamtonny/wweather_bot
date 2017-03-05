#!/usr/bin/env python3
# coding=utf-8


def represent_int(num):
    """isdigit analog for all str. additional testing for
    entry into the range [0-10], because query return max 10 elems.
    See 'setDays' method.
    """
    try:
        int(num)

        if -1 < int(num) < 11:
            return True

        return False
    except ValueError:
        return False
