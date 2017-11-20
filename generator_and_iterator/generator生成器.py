#! /user/bin/python/
# -*-coding:utf-8 -*-

print(range(5))
# print(xrange(5))

"""
    
    yield:普通函数添加yield 成为生成器 ，yield的作用是保留上一次执行的状态
    当寻找下一个yield不存在时程序报错 Traceback (most recent call last):
"""

# def xranage():
#     print(11)
#     yield(1)
#     print(22)
#     yield (2)
#
# #获取生成器对象
# r=xranage()
# #寻找第一个yield
# ret=r.next()
# print(ret)
# #寻找第二个yield
# ret=r.next()
# print(ret)
#寻找第三个yield 此时yield不存在 程序报错
# ret=r.next()
# print(ret)

#手动实现xranage原理
def myxranage(n):
    print ("start",n)
    start=0
    while True:
        if start >n:
            return
        else:
            yield start
            start +=1

mr=myxranage(5)
ret = mr.next()
print(ret)
ret = mr.next()
print(ret)
ret = mr.next()
print(ret)
ret = mr.next()
print(ret)
ret = mr.next()
print(ret)
ret = mr.next()
print(ret)
# for i in range(5):
#     ret = mr.next()
#     print(ret)
