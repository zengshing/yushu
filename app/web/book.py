
#-*- coding:utf-8 _*-
"""
@author:star
@file: book.py
@time: 2018/08/05
"""


from flask import jsonify, request
from app.libs.utils import is_isbn_or_key
from app.spider.yushu_book import YunShuBook
from app.web import web
from app.forms.book import SearchForms


@web.route('/book/search')
def search():
    '''
    :param q:  key words, or isbn
    :param page:  specified page
    :param ?q=isbn&page=1
    :return: book object
    '''
    form = SearchForms(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YunShuBook.search_by_isbn(q)
        else:
            result = YunShuBook.search_by_kw(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
