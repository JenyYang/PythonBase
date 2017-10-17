#! /user/bin/python/
# -*-coding:utf-8 -*-
"""
1、打开文件
    open( 文件名，打开模式，编码) 默认是只读模式  r只读模式 r+ 读写 w 只写 不存在创建 存在清空内容 w+ 写读 x只写（文件不存在创建 存在则报错） x+ 写读
            a追加 可写 不存在创建 存在则追加内容  a+写读  a在文件打开的同时指针已经移到文件的最后
2、操作文件
3、关闭文件

python3特性：文件可以字节方式打开 rb 只读 以字节形式读取
"""
#打开文件
# f=open("file.txt",encoding="utf-8")
# #读取文件
# data=f.read()
# #关闭文件
# f.close()
# print(data)
#
# f1=open("file.txt","a",encoding="utf-8")
# f1.write("还说的就是")
# f1.close()
# f=open("file.txt","rb")
# #读取文件
# data=f.read()
# #关闭文件
# f.close()
# print(data)

#tell 获取当前指针位置   seek调整指针位置


#文件操作
#复制文件  使用with 打开文件 不必手动关闭文件 将会自动给关闭 还可以同时 打开两个文件 在大文件复制中大大的解决了内存占用过大的问题
# with open("file.txt","r",encoding="utf-8") as f1,open("cfile.txt","w",encoding="utf-8") as f2:
#     for line in f1:
#         print(line)
#         f2.write(line)
#         f2.flush()#将内存中的内容刷到硬盘上

with open("file.txt","r+") as f:
    data=f.read()
    # print(data)
    print(f.tell())
    f.seek(2)
    f.write("ggg")