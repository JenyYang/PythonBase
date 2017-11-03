#! /user/bin/python/
# -*-coding:utf-8 -*-
"""
我是.py文件的注释
"""
dict_vars = vars()
print(dict_vars)
# # for i in vars():
# #     print(i)
"""

_loader_

_builtins_：内置函数在builtins里面
_spec_

_doc_
    .py文件的注释 

_package_：导入py文件所在的文件夹路径 当前文件除外 当前文件为none
_cached_：python3中新增属性 缓存  导入的其他模块哟缓存 当前文件为None
_name_：只有执行对应py文件时__name__=="__main__" 否则__name__=所属模块名
_file_：本身自己文件的绝对路径
"""
import sys
import os

print(__file__)
# 添加sys.path路径
"""
1、调用os.path.dirname()传入__file__当前文件路径获取到上级目录
2、调用os.path.join(上级目录，要拼接的路径)将两个路径拼接在一起得到要添加的路径
3、调用sys.path.append(添加的路径) 将路径添加到sys.path中
这样添加路径的有点是无论以后包名怎样改都不会影响文件的导入使用
"""
path1 = os.path.dirname(__file__)
path2 = "lib"
and_path = os.path.join(path1, path2)
print(and_path)
sys.path.append(and_path)

import myfile

"""
第三方模块的安装：
     1、软件管理工具安装pip3
        1、安装pip3 由于其依赖settools 所以要首先安装settools
        2、命令行中执行pip3 install requests
     2、源码安装
        1、下载 http://docs.python-requests.org/en/master/
        2、解压
        3、进入目录
        4、执行python setup.py install
"""
import requests
import json

"""
requests模块：
    用途：发送http请求 （用py模拟浏览器浏览网页）
"""
# url=http://www.weather.com.cn/adat/sk/101010500.html
# requests 的使用
response = requests.get("http://www.weather.com.cn/adat/sk/101010500.html")
response.encoding = "utf-8"  # 指定编码格式
result = response.text  # 获取返回的数据内容
dic_result = json.loads(result)#loads方法字符串内部必须是双引号
print(result)
print(dic_result)
