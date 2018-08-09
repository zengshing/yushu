#-*- coding:utf-8 _*-
"""
@author:star
@file: test2.py
@time: 2018/08/09
"""
import time
from werkzeug.local import LocalStack
from threading import Thread

my_stack = LocalStack()
my_stack.push(1)
print(my_stack.top)

def worker():
    print(my_stack.top)
    my_stack.push(2)
    print(my_stack.top)

T = Thread(target=worker, name='test')
T.run()
time.sleep(1)
print(my_stack.top)