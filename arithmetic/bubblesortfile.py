#!/user/bin/pyhton/
# -*-coding:utf-8 -*-
#冒泡排序
# def bubblesort(args):
#     for j in range(len(args)-1):#控制整个循环的次数
#         for i in range(len(args)-(j+1)):#控制每次循环的次数
#             if args[i]>args[i+1]:
#                 #交换位置
#                 temp=args[i]
#                 args[i]=args[i+1]
#                 args[i+1]=temp
#     return args
# li=[88,56,87,34,67,99,189,90,33]
# new_li=bubblesort(li)
# print(new_li)

#递归运用
# def f(args1,args2):
#     print(args1)
#     args1=args1+args2
#     if args1<10000:
#      f(args2,args1)
# f(0,1)

#利用递归获取斐波那契数列的第十个数
def f1(depth,a1,a2):
    if depth==10:
        return a1
    a3=a1+a2
    r=f1(depth+1,a2,a3)
    return r
ret=f1(1,0,1)
print(ret)