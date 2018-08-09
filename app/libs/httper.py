#-*- coding:utf-8 _*-
"""
@author:star
@file: httper.py
@time: 2018/08/05
"""

import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        result = requests.get(url)
        if result.status_code != 200:
            return {} if return_json else ''
        else:
            return result.json() if return_json else result.text


