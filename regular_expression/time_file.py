#! /user/bin/python/
# -*-coding:utf-8 -*-

"""
time 模块:
    1、sleep(数字) 程序终止指定时间
    2、time.time() 获取时间戳
    3、time.ctime() 获取当前系统时间的字符串格式 添加时间戳参数 是将指定的时间戳转换成字符串格式
datetime :

lib下的site-packages  存放所有第三方的库
sys模块：解释器相关的操作
    1、sys.exit(n) 退出程序  退出程序可以直接用exit(信息)  正常退出n=0
    2、sys.path.append(路径) 添加导入路径
 os模块：提供系统相关的操作
    os.path.join(path1,...)将多个路径组合返回，拼接路径
    os.stat(路径/文件名) 获取文件或目录信息

hashlib加密：代替md5和sha模块，主要提供了SHA1，SHA224，SHA256，SHA384，SHA512，MD5算法

"""

# md5加密不能反解
import hashlib
import time

hash_md5 = hashlib.md5(bytes(str(time.time()), encoding="utf-8"))
hash_md5.update(bytes("yang", encoding="utf-8"))
print(hash_md5.hexdigest())
