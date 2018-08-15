#-*- coding:utf-8 _*-
"""
@author:star
@file: book.py
@time: 2018/08/07
"""

from sqlalchemy import Column, VARCHAR, Integer, Float, String, Text, DATETIME
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(VARCHAR(80), unique=True, nullable=False)
    author = Column(VARCHAR(50), nullable=True, default='佚名')
    description = Column(Text, nullable=True)
    price = Column(Float(10))
    pages = Column(Integer)
    isbn = Column(String(20), unique=True, nullable=False)
    binding = Column(String(20))
    publisher = Column(String(100))
    pubdate = Column(DATETIME)
    image = Column(String(50))

    def __init__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        return '<Book {}>'.format(self.__name__)