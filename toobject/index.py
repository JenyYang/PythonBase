#! /user/bin/python/
# -*-coding:utf-8 -*-
from toobject.lib.orderClass import order_class

# order1=order_class()
# order1.countent="对象封装测试1"
# order2=order_class()
# order2.countent="对象封装测试2"
# order1.add_order()
# order2.update_order()

class A:
    def __init__(self):
        print("构造函数A")
        # super(E, self).__init__()
    def f(self):
        print("A")

class B:
    def __init__(self):
        print("构造函数B")
        # super(E, self).__init__()
    def f1(self):
        print("B")
class C(A,B):
    def __init__(self):
        print("构造函数C")
        super(C, self).__init__()

    def f2(self):
        print("C")
class D(B):
    def __init__(self):
        print("构造函数D")
        super(D, self).__init__()
    def f(self):
        print("D")

class E(D,C):
    def __init__(self):
        print("构造函数E")
        super(E,self).__init__()
    pass

e=E()
