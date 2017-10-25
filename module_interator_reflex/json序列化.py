#! /user/bin/python/
# -*-coding:utf-8 -*-
"""
urllib:用于发送http请求

json.loads(字符串) ：将指定的字符串转换成对应类型的数据类型
json.dumps(基本数据类型)：将制定的数据转换成字符串 元组dumps后是列表
"""
from urllib import request

f =request.urlopen("http://wthrcdn.etouch.cn/weather_mini?city=1000")
result=f.read()
print(result)

