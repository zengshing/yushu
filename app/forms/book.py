#-*- coding:utf-8 _*-
"""
@author:star
@file: book.py
@time: 2018/08/06
"""

from wtforms import Form, StringField, IntegerField
from wtforms.validators import NumberRange, Length, DataRequired

class SearchForms(Form):
    q = StringField(DataRequired(), validators=[Length(min=1, max=30)])
    page = IntegerField(DataRequired(), validators=[NumberRange(min=1, max=99)], default=1)

