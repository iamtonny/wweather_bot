#!/usr/bin/env python3
# coding=utf-8

from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    username = Column(String(100), unique=True)
    city = Column(String(100))
    num_display_days = Column(Integer)
    details = Column(Boolean)

    def __init__(self, telegram_id=None, username=None,
                 city=None, display_days=10, details=False):
        self.telegram_id = telegram_id
        self.username = username
        self.city = city
        self.num_display_days = display_days
        self.details = details

    def __repr__(self):
        return '<User %r>' % (self.username)
