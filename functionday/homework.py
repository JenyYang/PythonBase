#! /user/bin/python/
# -*-coding:utf-8 -*-
"""
1、简述普通参数、指定参数、默认参数、动态参数的区别
  (1)普通参数 调用函数时传递的实际参数按照顺序传递
  (2)指定参数 调用函数传递实参时指定代表的形参 这时可以不按照顺序传递参数 函数中接受实参时仍然可以按照形参列表顺序接受
  (3)默认参数 当函数参数列表中为形参设置了默认值时，调用函数时可以不传递已设置默认值的参数 如果传递了已有默认值的实参，那么函数中使用该参数时
    接收的是传递的实参，设置默认值得形参一定要放在参数列表的尾部
  (4)动态参数 *args 参数类型是tuple **kwargs 参数类型是dict **的动态参数 调用函数传递时必须以key=value的形式传递
        动态参数传递实参时 列表 字典 元组 作为实参时 如果实参前不加* 接受时会将整个数据作为一个参数 加* 会将数据中的每个元素作为一个参数
"""

#2、 写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。

def DesicionLen(args):
    if len(args)>5:
        return True
    else:
        return False
s="abcdefg34 22#￥ "
li=["12",23,{"k1":34,"k2":"aa"}]
tu=("aa",'bb',45,56,'mm','kk')
slen=DesicionLen(s)
lilen=DesicionLen(li)
tulen=DesicionLen(tu)
print(slen,lilen,tulen)

#3、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
s1="abcdefg34 22#￥    "
numcount=0# 数字个数
charcount=0 #字母个数
blankcount=0 #空格个数
othercount=0 #其他个数
def ReckonCount(args):
    for c in args:
        if c.isdigit():#判断是否是数字
            global numcount
            numcount+=1
        elif c.isalpha():#判断是否是字母
            global charcount
            charcount+=1
        elif c.isspace():#判断是否是空格
            global blankcount
            blankcount+=1
        else:#其他
            global othercount
            othercount+=1
ReckonCount(s1)
print(numcount,charcount,blankcount,othercount)
