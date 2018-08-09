#-*- coding:utf-8 _*-
"""
@author:star
@file: utils.py
@time: 2018/08/04
"""


def is_isbn_or_key(word):
    '''
    :param word:
    :return:
    '''
    isbn_or_key = 'key'

    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    short_word = isbn_or_key.replace('-', '')

    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key