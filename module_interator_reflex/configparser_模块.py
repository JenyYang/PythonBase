#! /user/bin/python/
# -*-coding:utf-8 -*-

"""
 configParser模块：
    1、导入configparser模块
    2、创建configparser对象 con = configparser.ConfigParser()
    3、读取文件到内存 re = con.read(文件名)
    4、方法使用
        1、获取所有的[xxx]类型的节点：con.sectons()
        2、获取对应节点下的所有key值：con.options(节点名)

    注意：读取的文件中键值之间：与=需统一使用不能交叉使用

"""

# 测试configparser模块使用

import ConfigParser

# 创建ConfigParser对象
con = ConfigParser.ConfigParser()
# 调用read方法读取文件内容到内存
con.read("config_ini")
# 调用sections（）方法获取所有的节点
con_node = con.sections()
print (con_node)
#items方法获取所有的键值对
code_result = con.items("yangruijing")
print(code_result)
#options方法获取所有的键
code_key= con.options("yangruijing")
print(code_key)

#获取键对应的值
code_value=con.get("yangruijing","gender")
print (code_value)

#has_section(节点名) 检查是否存在指定的节点 返回值是True或Flase

is_has=con.has_section("yangruijing")
print(is_has)

#add_section(节点名)

con.add_section("Marry")#添加节点 添加到了内存中
# 将内存中数据重新写入到文件中
con.write(open("config_ini","w"))

#remove_section(节点名) 删除指定的节点
con.remove_section("Marry")
#将修改的内存中的内容重新写入到文件中
con.write(open("config_ini","w"))

#has_option(节点名，键名)检查是指定节点下是否存在指定的键
is_option=con.has_option("yangruijing","age")
print(is_option)

#remove_option(节点名，键名) 删除指定的键值对

con.remove_option("yangruijing","gender")
 #将修改后的内存中的数据重新写入到文件中
con.write(open("config_ini","w"))

#set(节点名，键，值) 节点下不存在指定键值对则添加 存在则修改

con.set("yangruijing","gender","女")
con.write(open("config_ini","w"))

