#! /user/bin/ python
# -*- coding:utf-8 -*-

# 集合中所有元素进行分类
# li=[19,80,55,44,38,69,70,50,29,48,99]
# dict={
#     "k1":[],
#     "k2":[]
# }
# for i in li:
#     if i<=60:
#         dict["k1"].append(i)
#     else:
#         dict["k2"].append(i)
# print (dict);

"""
li=["alec","aric","Alex","Tony","rain"]
tu=("alec","aric","Alex","Tony","rain")
dict={"k1":"alec","k2":"aric","k3":"Alex","k4":"Tony","k5":"rain"}

查找以a或A开头 并以c结尾的元素
"""
# 集合操作
# li=["alec","aric","Alex","Tony","Alec"]
# for i in li:
#     if (i[0]=="a" or i[0]=="A") and i.endswith("c"):
#         print (i)
#     else:
#         continue;

# 元祖操作
# tu=("alec","aric","Alex","Tony","rain")
# for i in tu:
#     if (i[0] == "a" or i[0] == "A") and i.endswith("c"):
#           print (i)
#     else:
#          continue;

# 字典操作
# dict={"k1":"alec","k2":"aric","k3":"Alec","k4":"Tony","k5":"rain"}
# for i in dict:
#     v=dict[i]
#     v1=v.upper();
#     if v1.startswith("A") and v1.endswith("C"):
#         print ("{"+i+":"+v+"}")
#     else:
#         continue
# li = ["手机", "电脑", '鼠标垫', '游艇']
# value=input("请输入商品编号：")
# print (li[int(value)])

name="杨瑞静"
# print(name)
# for i in name:
#     print(i)
#     byte_list=bytes(i,"utf-8")
#     print(byte_list)
    # for b in byte_list:
    #     print(b)
    #     print(bin(b))
# b1=bytes(name,"utf-8")
# print(b1)
# name1=str(b1,encoding="utf-8")
# print(name1)
# b2=bytes(name,"gbk")
# print(b2)
# name2=str(b2,encoding="gbk")
# print(name2)

#字符串转换成list
# str="杨瑞静"
# li=list(str)
# print(li)

#元祖转换成list
# tu=("yang","rui","jing")
# li=list(tu)
# print(li)

#字典转换成list
# dict={"k1":"yang","k2":"rui","k3":"jing"}
# li=list(dict.items())
# print(li)

#list追加
# li=["a","b"]
# li.append("c")
# print(li)

#list 清除
# li=["a","b"]
# print(len(li))
# li.clear()
# print(len(li))

# li=["yang","rui"]
# print(li)
# # 字符串
# s="jing"
# li.extend(s)
# print(li)
# # 集合
# li1=["123","234"]
# li.extend(li1)
# print(li)
# # 字典 默认扩充的内容的key值 因为内部循环默认是key循环
# dict={"k1":"abc","k2":"nbm"}
# li.extend(dict)
# print(li)
# # 指定以字典value扩充
# li.extend(dict.values())
# print(li)
# #指定以字典item扩充 扩充到list中的每一个元素都是元祖形式
# li.extend(dict.items())
# print(li)
# # 元祖
# tu=("lll","kkk")
# li.extend(tu)
# print(li)

#list自身翻转
# li=["1243","mmmm",90]
# print(li)
# li.reverse()
# print(li)
#list 指定位置插入元素
# li=["1243","mmmm"]
# print(li)
# li.insert(0,123)
# li.insert(2,"abc")
# li.insert(len(li),"end")
# print(li)

#list 索引

# li=["杨","瑞","静"]
# #根据索引获取指定位置的元素
# s=li[0]
# print(s)
# #获取指定元素的索引
# i=li.index("瑞")
# print(i)
# li=["杨","瑞","静"]
# s=li[0:2]
# print(s)



#元组
"""
 1 、创建和转换
 2、特有方法
    count index
3、 嵌套
4、元组特性 元组元素不可修改
"""
# tu=(22,"aa","nn","aa",["aa",{"k1":"aa"}],"aa")
# i=tu.index("aa",2,len(tu))
# print(i)
# i1=tu.index("bb")
# print(i1)
# i=tu.count("aa")
# print(i)
# tu=(22,"aa",["bb",{"k1":"yang"}])
# tu[2].append("cc")
# tu[2][1]["k1"]="样"
# print(tu)
# tu[1]="abc"
# dic1={"k1":123,"k2":"abc","k3":[123,456]}
# #字符串转换成元组
# t=tuple("abcdef")
# # 列表转换成元组
# tu=tuple(["123",345,"abc"])
# # 字典转换成元组
# # 默认转换 keys
# tu0=tuple(dic1)
# # values 转换成元组元素
# tu1=tuple(dic1.values())
# #items 转换成元组元素 没对键值对作为一个元组成为一个元组元素
# tu2=tuple(dic1.items())
# print(t)
# print(tu0)
# print(tu)
# print(tu1)
# print(tu2)
#字典
"""
1、创建
2、内部功能
    fromkeys
"""
# li=["aaa","bb"]
# dic=dict(enumerate(li))
# # for k enumerate li:
# #     dic[k]=v
# print(dic)
# dic={"k1":"123","k2":"234"}
# dic.fromkeys()
#调用fromkeys方法创建字典数据
dic=dict.fromkeys(["k1","k2","k3"],"alex")
#分别用传统方式和fromkeys方法创建字典数据 value为列表类型
dict1={"k1":[],"k2":[]}
dict2=dict.fromkeys(["k1","k2"],[])
print(dict1)
print(dict2)
#对两种方式创建的两个字典数据追加value值 区别 传统方式创建的只给指定的key追加value 而 fromkeys方法创建的虽然指定了要追加
#value值得键key 结果为每一个键所对应的value都追加了值,之所以出现这样的区别是因为fromkeys方法创建字典每一个key公用了一个列表数据
dict1["k1"].append("aa")
dict2["k1"].append("bb")
print(dict2)
print(dict1)
print(dic)
#自己实现公用一个列表字典数据的变化
li=[]
dic3={"k1":li,"k2":li}
print(dic3)
dic3["k1"].append("ccc")
print(dic3)