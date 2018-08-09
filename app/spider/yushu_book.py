#-*- coding:utf-8 _*-
"""
@author:star
@file: yushu_book.py
@time: 2018/08/05
"""

from app.libs.httper import HTTP
from flask import current_app

class YunShuBook:
    isbn_api_url = "http://t.yushu.im/v2/book/isbn/{}"
    kw_api_url = "http://t.yushu.im/v2/book/search?q={}&start={}&count={}"

    #调用类变量
    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_api_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_kw(cls, kw, page=1):
        start = cls.calculate_startpoint(page)
        url = cls.kw_api_url.format(kw, start, current_app.config['PRE_PAGE'])
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_startpoint(page):
        count = current_app.config['PRE_PAGE']
        start_point = (page - 1) * count
        return start_point
