#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 16:45
# @Author : LJY
# @Brief :
# @File : chapter3_4.py
# @PROJECT_NAME : web_develop
# @Software: PyCharm
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