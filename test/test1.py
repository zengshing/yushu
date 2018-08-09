#-*- coding:utf-8 _*-
"""
@author:star
@file: test1.py
@time: 2018/08/08
"""


# class A():
#
#     def __init__(self):
#         pass
#
#     def __enter__(self):
#
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#     def query_data(self):
#         print('get all data.')


#from flask import Flask, current_app
#
#
# app = Flask(__name__)
# app.config.from_object('config')
# with app.app_context():
#     a = current_app
#     print(a.config['DEBUG'])

class Employee():
    def __enter__(self):
        print("I'm enter.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("I'm exit")
        return True

    def print(self):
        print("you are welcome.")


try:
    with Employee() as e:
        1/0
        e.print()

except e:
    print(e)
