#-*- coding:utf-8 _*-
"""
@author:star
@file: test7.py
@time: 2018/08/12
"""


from werkzeug.local import LocalStack, LocalProxy

user_stack = LocalStack()
user_stack.push({'name':'alice'})
user_stack.push({'name':'bob'})

def get_user():
    return user_stack.pop()


user = LocalProxy(get_user)
print(user.get('name'))
print(user.get('name'))

