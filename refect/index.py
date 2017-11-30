#! /user/bin/python/
# -*-coding:utf-8 -*-
inp = input("请输入url:")
inp_module,inp_funct = inp.split("/")
#导入模块
m=__import__("lib."+inp_module,fromlist=True)

if hasattr(m,inp_funct):#判断模块中是否存在输入的方法
    #从模块中获取到该方法
    target_func=getattr(m,inp_funct)
    #执行方法获取返回值
    ret=target_func()
    print (ret)
else:
    print ("404")
