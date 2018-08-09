#-*- coding:utf-8 _*-
"""
@author:star
@file: __init__.py
@time: 2018/08/05
"""

from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book