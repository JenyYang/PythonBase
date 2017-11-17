#! /user/bin/python/
# -*-coding:utf-8 -*-

# import shutil
#
# #copyfileobj复制文件 w清空原有内容写入新内容 a保留原有内容追加新内容
#
# shutil.copyfileobj(open("myuser.xml","r"),open("cpmyuser.xml","w"))
# shutil.copyfileobj(open("user.xml","r"),open("cpmyuser.xml","a"))


# #zipfile 压缩文件
# import zipfile
# #w清空压缩包原有内容 a 追加新内容
# z=zipfile.ZipFile("user.zip","w")
# z=zipfile.ZipFile("user.zip","a")
# #将要压缩的文件写入到压缩包中
# z.write("cymyuser.xml")
# z.close()


# import zipfile
#
# z=zipfile.ZipFile("user.zip","r")
# #解压所有的文件
# z.extractall()
# #解压指定文件
# z.extract("user.xml")
# #获取解压的所有文件的文件名列表
# r=z.namelist()
# print(r)
# z.close()

#tar文件压缩和解压

# import tarfile
# #创建tarfile对象
# tar=tarfile.TarFile("user1.tar","w")
# #添加要压缩的文件 arcname设置压缩文件后的文件名
# tar.add("user.xml",arcname="user1.xml")
# tar.add("myuser.xml",arcname="myuser1.xml")
# tar.close()

#tar文件解压
import tarfile
tar=tarfile.TarFile("user1.tar","r")
#user1是设置解压后的文件地址
# tar.extractall("user1")
#获取解压的所有成员
r=tar.getmembers()
print (r)
#解压单个文件文件名必填 解压路径可写可不写
tar.extract("myuser1.xml","lib")
tar.close()

