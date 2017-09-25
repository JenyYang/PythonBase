#! /user/bin/python/
# -*-coding:utf-8 -*-

"""
可代替一些简单的函数
定义方式   函数名（变量名）=lambda 参数（多个用逗号隔开）：返回值
"""
def f1(a1,a2):
    return a1+a2
f2=lambda a1,a2:a1+a2
ret=f1(1,2)
ret1=f2(2,3)
print(ret)
print(ret1)
