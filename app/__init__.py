#-*- coding:utf-8 _*-
"""
@author:star
@file: __init__.py
@time: 2018/08/05
"""

from flask import Flask
from app.models.book import db
from app.web import *

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app

def register_blueprint(app):
    app.register_blueprint(web)



