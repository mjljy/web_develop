#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 13:32
# @Author : LJY
# @Brief :
# @File : chapter3_2.py
# @PROJECT_NAME : web_develop
# @Software: PyCharm
#http://reddit.com/r/flask+lisp   查看多个社区的帖子？？？？？
#flask自定义转换器
#可能会出现限制用户访问的规则的场景，那么这个时候，就需要过滤指定用户，所以可以使用转换器实现。
#转换器：
# 转换器的本质是：通过正则表达式匹配路由地址
# class BaseConverter(object):
# 父类 regex = "[^/]+"
# ^ 匹配字符串开头
# + 表示匹配子表达式（非/）一次或多次
# /：表示URL中常见/
# [^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
# coding=utf-8
import urllib

from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class ListConverter(BaseConverter):

    def __init__(self, url_map, separator='+'):
        super(ListConverter, self).__init__(url_map)
        self.separator = urllib.unquote(separator)

    def to_python(self, value):
        return value.split(self.separator)

    def to_url(self, values):
        return self.separator.join(BaseConverter.to_url(self, value)for value in values)

app.url_map.converters['list'] = ListConverter
@app.route('/list1/<list:page_names>/')
def list1(page_names):
    return 'Separator: {0} {1}'.format('+', page_names)

@app.route('/list2/<list(separator=u"|"):page_names>/')
def list2(page_names):
    return 'Separator: {0} {1}'.format('|', page_names)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
