
#-*- coding:utf-8 _*-
"""
@author:star
@file: book.py
@time: 2018/08/05
"""


from flask import request, jsonify, render_template
from app.web import web
from app.forms.book import BookForm
from app.lib.helper import is_isbn_keyword
from app.spider.Yunshu import YuShuBook
from app.view_models.book import BookCollection


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu = YuShuBook()
    book = BookCollection()
    yushu.search_by_isbn(isbn)
    book.fill(yushu, isbn)
    return render_template('book_detail.html', book=book, wishs='', gifts='')


@web.route('/book/search')
def search():
        f = BookForm(request.args)
        isbn_keyword = ''
        q = ''
        page = ''
        books = BookCollection()
        yushu = YuShuBook()

        if request.method == 'GET' and f.validate():
            q = f.q.data
            page = f.page.data
            isbn_keyword = is_isbn_keyword(q)

            if isbn_keyword == 'isbn':
                yushu.search_by_isbn(q)

            elif isbn_keyword == 'keyword':
                yushu.search_by_keyword(q, page)
            books.fill(yushu, q)

        return render_template('search_result.html', books=books)
