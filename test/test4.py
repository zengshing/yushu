#-*- coding:utf-8 _*-
"""
@author:star
@file: test4.py
@time: 2018/08/11
@access: https://www.cnblogs.com/chengd/articles/7770898.html
"""

# import threading
# from werkzeug.local import Local
# import time
#
# l = Local()
# l.__storage__
# def add_arg(arg, i):
#     l.__setattr__(arg, i)
# for i in range(3):
#     arg = 'arg' + str(i)
#     t = threading.Thread(target=add_arg, args=(arg, i), name='thread'+str(i))
#     t.start()
#     time.sleep(1)
#
#
# print(l.__storage__)


from werkzeug.local import LocalStack, LocalProxy
import logging, random, threading, time
# 定义logging配置
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
# 生成一个LocalStack实例_stack
_stack = LocalStack()
# 定义一个RequestConetxt类，它包含一个上下文环境。
# 当调用这个类的实例时，它会将这个上下文对象放入
# _stack栈中去。当退出该上下文环境时，栈会pop其中
# 的上下文对象。
class RequestConetxt(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __enter__(self):
        _stack.push(self)
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            _stack.pop()
    def __repr__(self):
        return '%s, %s, %s' % (self.a, self.b, self.c)
# 定义一个可供不同线程调用的方法。当不同线程调用该
# 方法时，首先会生成一个RequestConetxt实例，并在这
# 个上下文环境中先将该线程休眠一定时间，之后打印出
# 目前_stack中的信息，以及当前线程中的变量信息。
# 以上过程会循环两次。
def worker(i):
    with request_context(i):
        for j in range(2):
            pause = random.random()
            logging.debug('Sleeping %0.02f', pause)
            time.sleep(pause)
            logging.debug('stack: %s' % _stack._local.__storage__.items())
            logging.debug('ident_func(): %d' % _stack.__ident_func__())
            logging.debug('a=%s; b=%s; c=%s' %
                          (LocalProxy(lambda: _stack.top.a),
                           LocalProxy(lambda: _stack.top.b),
                           LocalProxy(lambda: _stack.top.c)))
    logging.debug('Done')
# 调用该函数生成一个RequestConetxt对象
def request_context(i):
    i = str(i+1)
    return RequestConetxt('a'+i, 'b'+i, 'c'+i)
# 在程序最开始显示_stack的最初状态
logging.debug('Stack Initial State: %s' % _stack._local.__storage__.items())
# 产生两个线程，分别调用worker函数
for i in range(2):
    t = threading.Thread(target=worker, args=(i,))
    t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
# 在程序最后显示_stack的最终状态
logging.debug('Stack Finally State: %s' % _stack._local.__storage__.items())