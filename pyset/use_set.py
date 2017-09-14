#! /user/bin/ python
# -*- coding:utf-8 -*-
#set 不允许重复的集合 list 允许重复可修改 元组 允许重复 不可修改
"""
1、创建set
2、转换
"""
# s=set()#创建空集合
#s=set(可迭代的数据)
#s={"1","22"}

# #字符串转换
# s="aabcnd"
# se=set(s)
# print(se)
# # list 数据转换
# li=["aa","bb","aa",123]
# se1=set(li)
# print(se1)
# #元组转换
# tu=("ab",123,"bc","ab")
# se2=set(tu)
# print(se2)
# #字典转换
# dic={"k1":123,"k2":123,"k3":"abc"}
# se3=set(dic)
# print(se3)
# se4=set(dic.values())
# print(se4)
# se5=set(dic.items())
# print(se5)
# for s in se5:
#     print(type(s))
#add
# se1={}
# print(type(se1))#这种方式创建默认类型是dict
# se=set()
# se.add(11)
# se2={22,44,11}
# se3=se2.difference(se)# 找出se2中存在se中不存的元素的集合
# print(se)
# print(se3)
# se2.difference_update(se)# 删除 se2中与se中重复的元素
# print(se2)

#clear
se={"aa","bb",123,344}
print(se)
se.clear()
print(se)

#dicard 移除集合中的指定元素 不存在不报错 remove 在移除元素不存在的时候报错
se1={"11",23,34}
se2={"aa",12,"bc"}
se1.discard("11")
print(se1)


#intersection 获取 A和B 中都存在的元素集合
section={11,22,33,44}
section1={11,33,"aa","bb"}
section2={11,22,33,44,55}
ret=section.intersection(section1)
print(ret)

# isdisjoint 判断两个集合中是否有相同的元素 有交集返回false 没有交集返回true
fl=section.isdisjoint(section1)
print(fl)

# issubset 判断A 是否是B的子集 是返回true 反之返回false
fl1=section.issubset(section1)
fl2=section.issubset(section2)
print(fl1)
print(fl2)
# issuperset 判断A是否是B的父集合 即 A中是佛包含了B中所有的元素  是返回true 反之返回false
fl3=section.issuperset(section1)
fl4=section2.issuperset(section)
print(fl3)
print(fl4)
#pop 移除一个元素 移除并返回要移除的元素值
print(section)
p=section.pop()
print(p)
print(section)
p1=section.pop()
print(p1)

#symmetric_difference 对称交集  返回对称交集集合 不改变原有集合
sym_set=section2.symmetric_difference(section1)
print(sym_set)
print(section2)
#symmetric_difference 对称交集 并更新原有的调用集合
print(section1)
section1.symmetric_difference_update(section2)
print(section1)
#union 取并集  原集合不变 返回新的集合
print(section1)
print(section2)
set_union=section1.union(section2)
print(set_union)
print(section1)
print(section2)
# update更新  改变要更新集合的元素
print(section)
section.update(section2)
print(section2)
print(section)