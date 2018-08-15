#-*- coding:utf-8 _*-
"""
@author:star
@file: test8.py
@time: 2018/08/12
"""


from functools import partial

def sum(*args):
    sum = 0
    for i in args:
        sum += i

    return  sum

sum_10 = partial(sum, 10)
sum_10_20 = partial(sum, 10, 20)
print('sum enter:{}'.format(sum))
print('sum_10 enter:{}'.format(sum_10))
print(sum(1,2,3,4,5))
print(sum_10(1,2,3,4,5))
print(sum_10_20(1,2,3,4,5))



