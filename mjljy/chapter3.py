#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:LJY
# software: Vscode
from flask import Flask
app = Flask(__name__)  #引入Flask类 实现一个WSGI应用
# WSGI:Web Server Gateway Interface WSGI也主要分为两个程序部分：服务器部分和应用程序部分
#实现一个实例


#服务器返回函数
#函数在返回的时候被执行  先执行装饰器的内部函数  再执行被装饰的函数
#第一层 传递 被装饰的函数  返回第二层函数 第二层函数传递被装饰函数的参数 返回被装饰的函数
@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == "__main__":
    app.debug = True
    app.run(host="127.0.0.1", port=9000)
    #这个demo开启了一个本地web服务器   外部来访问的时候 还会返回 东西
    #既包含了service 也包含了 application
