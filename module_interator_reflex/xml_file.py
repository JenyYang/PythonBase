#! /user/bin/python/
# -*-coding:utf-8 -*-
"""
XML:实现不同语言或程序之间进行数据交换的协议
 
"""
"""
import requests
from xml.etree import ElementTree as EF

# 检查qq是否在线

r = requests.get("http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=1129223929")
result = r.text
# print(result)
#调用XML 中的ElementTree中的XML 解析xml格式的字符串
node = EF.XML(result)
if node.text=="Y":
     print("在线")
else:
    print("不在线")
# print(node.text)
"""

"""
import requests
from xml.etree import ElementTree as ET

# 获取列车时刻表
r = requests.get(
    "http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=K234&UserID=")
result = r.text
print(result)
root = ET.XML(result)
for node in root.iter("TrainDetailInfo"):#iter找子节点
    print(node.find(""))#find 获取子节点内容

"""
from xml.etree import ElementTree as ET

"""
# open打开文件读取xml文件


# result=ET.XML(open("user.xml","r",encoding="utf-8").read())
# for node in result:
#     print(node.tag,node.attrib,node.find("age").text,node.find("gender").text)
"""

"""
#  #parse 解析xml文件 这种解析方式可以修改文件内容
r = ET.parse("user.xml")
#获取根节点
root = r.getroot()
for node in root:
    print(node.tag, node.attrib, node.find("age").text, node.find("gender").text)
    # 修改xml文件中节点的内容
    new_age = int(node.find("age").text) + 1
    node.find("age").text=str(new_age)
    #添加节点属性
    node.set("school","华北理工大学")
    #删除节点属性
    del node.attrib["school"]
    #添加新子节点 方式一
    school=ET.SubElement(node,"school")
    school.text="华北理工大学"
    #添加新子节点 方式二
    home=node.makeelement("home", {"name":"home"})
    home.text="河北省 邯郸市"
    node.append(home)
    #创建节点方式3
    # node1=ET.Element("node1",{"name":"node1"})
    node.find("node1").text="node1"
    #将创建的节点添加到指定的父节点下 extend为当前节点追加n个节点
    # node.append(node1)
    #remove删除子节点
    #findall获取所有的子节点
    #get获取当前节点的属性值
    #set为当前节点设置/修改属性值


#修改的xml内容修改的是内存中读取的内容，需将内容重新写入到xml文件 文件中的内容才会更新
r.write("user.xml",encoding="utf-8",xml_declaration=True)
"""
"""
#写xml文件
# 1、导入包
# 2、创建根节点
# 3、创建根节点的子节点
# 4、生成文档
# 5、将文档内容写入到文件中
#导入包
from xml.etree import ElementTree as ET

# 创建根节点
new_xml = ET.Element("userlist")
#创建根节点的子节点
for i in range(2):
    #SubElement(父节点，节点名（tag）,属性（attrib={属性名:属性值}）)
    name=ET.SubElement(new_xml,"user",attrib={"name":"ruijing"+str(i)})
    age=ET.SubElement(name,"age")
    age.text=str(i+20)
#生成文档
et=ET.ElementTree(new_xml)
#将文档内容写入到文件中
et.write("myuser.xml",encding="utf-8",xml_declaration=True)
"""

#xml.minidom提供了添加节点缩进的方法toprettyxml

