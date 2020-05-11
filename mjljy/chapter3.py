#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:LJY
# software: Vscode
from flask import Flask
app = Flask(__name__)  #引入Flask类 实现一个WSGI应用
# WSGI:Web Server Gateway Interface WSGI也主要分为两个程序部分：服务器部分和应用程序部分
#实现一个实例

@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
    #这个demo开启了一个本地web服务器   外部来访问的时候 还会返回 东西
    #既包含了service 也包含了 application
