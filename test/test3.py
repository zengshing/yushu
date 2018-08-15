#-*- coding:utf-8 _*-
"""
@author:star
@file: test3.py
@time: 2018/08/11
"""

from greenlet import greenlet
def test1():
    print(12)
    gr2.switch()
    print(34)

def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()