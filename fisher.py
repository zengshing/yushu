#-*- coding:utf-8 _*-
"""
@author:star
@file: httper.py
@time: 2018/08/05
"""

from app import create_app

app = create_app()

def main():
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'], threaded=True)

if __name__ == "__main__":
    main()