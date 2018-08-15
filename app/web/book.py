
#-*- coding:utf-8 _*-
"""
@author:star
@file: book.py
@time: 2018/08/05
"""


from flask import jsonify, request
from app.libs.utils import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection
from app.web import web
from app.forms.book import SearchForms

from app.libs.non_local import n

@web.route('/book/search')
def search():
        f = SearchForms(request.args)
        isbn_keyword = ''
        q = ''
        page = ''
        book = BookCollection()
        yushu = YuShuBook()

        if request.method == 'GET' and f.validate():
            q = f.q.data
            page = f.page.data
            isbn_keyword = is_isbn_or_key(q)

            if isbn_keyword == 'isbn':
                yushu.search_by_isbn(q)

            elif isbn_keyword == 'keyword':
                yushu.search_by_keyword(q, page)
            book.fill(yushu, q)


@web.route('/test')
def test():
    print(n.view)
    n.view = 2
    print('----------------')
    print(getattr(request, 'view', None))
    setattr(request, 'view', 2)
    print('----------------')
    return ''