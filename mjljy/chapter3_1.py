#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 10:13
# @Author : LJY
# @Brief :
# @File : chapter3_1.py
# @PROJECT_NAME : web_develop
# @Software: PyCharm
from flask import Flask
app = Flask(__name__)
# @app.route('/example/1/')
# @app.route('/example/2/')
# @app.route('/example/3/')
# def example(id):
#      return 'example:{ }'.format(id)
#      # return "OK"
#这种使用方法 应该是flask的特殊使用方法

@app.route('/example/<id>/')
# @app.route('/<id>/<cmd>/')
# def hello_world(id,cmd):
#     print "id,cmd",id,cmd
#     print type(list(id))
#     print type(str(cmd))
#     env_lsit = []
# @app.route('/<any(a, b):page_name >/ ')
# <id>
# 它使用了特殊的字段标记<variable_name> ，默认类型是字符串。
# people/?name=a, /people/?name=b, 这样就可以通过“ name= request.args.get('name') "
#post 方法 name= request。form.get('name')
def wxample(id):
       return 'example:{0}'.format(id)
if __name__ == "__main__":
    app.debug = True
    app.run(host="127.0.0.1", port=9000)
    #这个demo开启了一个本地web服务器   外部来访问的时候 还会返回 东西
    #既包含了service 也包含了 application
