#! /user/bin/python/
# -*-coding:utf-8 -*-

#获取一个任意位数的随机验证码
import random
def getrandomcode(args):
    temp=""
    for i in range(args):
        rad1=random.randrange(0,4)
        if rad1/2==0:
            temp=temp+str(rad1)
        else:
            rad2=random.randrange(65,91)#获取随机大写字母
            c=chr(rad2)
            temp=temp+c
    return temp
randomcode=getrandomcode(2)
print(randomcode)


