#! /user/bin/python/
# -*-coding:utf-8 -*-

"""
字符串格式化
    1、百分号方式
        .perssion 浮点数精度
    2、format方式格式化



"""
# %字符串拼接
# s = "I am %s ,age %d" % ("yangruijing", 27)
# print(s)
# format格式化
s = "I am {} ,age {}".format("alex", 20)
s1 = "I am {} ,age {}".format(*["Tom", 20])
s2 = "I am {name} ,age {age}".format(**{"name": "Jenny", "age": 20})
s3 = "I am {name:s} ,age {age:d}".format(**{"name": "Mary", "age": 21})
print(s)
print(s1)
print(s2)
print(s3)
