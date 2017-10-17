#! /user/bin/python/
# -*-coding:utf-8 -*-

"""
装饰器原理：
@函数名  作用
    1、执行函数并且将其下面的函数名作为参数
       @函数名
       def f1()
    2、将函数的返回值赋值给下面的函数

装饰器传递两个参数
 装饰器传递N个参数

"""
#全能装饰器 传递任意个数的参数
def outer(fucn):
    def inner(*args,*kwargs):
        print("before")
        ret=fucn(*args,*kwargs)
        print("after")
        return ret
    return inner

#多个装饰器装饰同一个函数  这时效果是先执行最上面的装饰器

"""
装饰器课下任务
1、单个装饰器多个函数的应用 并文字描述执行步骤
2、多个装饰器的应用 并文字描述执行步骤 
"""
