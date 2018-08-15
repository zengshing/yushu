#-*- coding:utf-8 _*-
"""
@author:star
@file: yushu_book.py
@time: 2018/08/05
"""

from app.libs.httper import HTTP
from flask import current_app

class YuShuBook:
    isbn_api_url = "http://t.yushu.im/v2/book/isbn/{}"
    kw_api_url = "http://t.yushu.im/v2/book/search?q={}&start={}&count={}"

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        print(url)
        http = HTTP()
        data = http.get(url)
        print(data)
        self.__fill_single(data)

    def search_by_keyword(self, kw, page):
        count = current_app.config['PAGE_COUNT']
        start = self.calculate_starts(page, count)
        url = self.keyword_url.format(kw, start, count)
        http = HTTP()
        data = http.get(url)
        self.__fill_collection(data)

    def __fill_single(self, data):
        self.total = 1
        self.books = [data]

    def __fill_collection(self, data):
        self.total = data.get('total', 0)
        self.books = data['books']

    def calculate_starts(self, page, count):
        return (page - 1) * count