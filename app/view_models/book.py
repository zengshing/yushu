#-*- coding:utf-8 _*-
"""
@author:star
@file: book.py
@time: 2018/08/15
"""

# !/usr/bin/env python
# coding:utf-8

"""
@author: star
@contact: zengshingx@163.com
@software: PyCharm
@file: book.py
@time: 2018/8/15 9:43
"""


class BookViewModel():

    def __init__(self, book):
        self.title = book.get('title')
        self.author = '、'.join(book.get('author'))
        self.translator = '、'.join(book.get('translator')) or ''
        self.isbn = book.get('isbn')
        self.price = book.get('price') or ''
        self.pages = book.get('pages') or ''
        self.binding = book.get('binding') or ''
        self.publisher = book.get('publisher') or ''
        self.pubdate = book.get('pubdate') or ''
        self.category = book.get('category') or ''
        self.summary = book.get('summary') or ''
        self.image = book.get('image')
        self.images = book.get('images')

    def __str__(self):
        return '<book.{title}, book.{author}>'.format(self.title, self.author)


class BookCollection():

    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, books, keyword):
        self.total = books.total
        self.books = [BookViewModel(book) for book in books.books]
        self.keyword = keyword