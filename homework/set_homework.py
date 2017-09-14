#! /user/bin/ python
# -*- coding:utf-8 -*-
#删除old中存在 new中不存在的 添加new中存在old中不存在的 更新old中和new中同时存在的
old_dict={"#1":11,"#2":22,"#3":100}
new_dict={"#1":33,"#4":22,"#7":100}
old_keys=old_dict.keys()
new_keys=new_dict.keys()
old_set=set(old_keys)
new_set=set(new_keys)
#old中存在 new中不存在
del_set=old_set.difference(new_keys)
#new 中存在 old中不存在
add_set=new_set.difference(old_set)
#new和old中同时存在
update_set=old_set.intersection(new_set)
print(del_set)
print(add_set)
print(update_set)
#遍历要删除的key值集合 删除字典中的对应元素
for de in del_set:
    old_dict.pop(de)
print(old_dict)
#遍历要添加的key值集合 在old字典中添加new字典中对应的元素
for ad in add_set:
    add_item=new_dict.get(ad)
    old_dict.update({ad:add_item})
    # old_dict.get(add_item)
print(old_dict)

#遍历要更新的key值集合 更新old中的元素value值为new中对应的
for new in update_set:
    old_dict[new]=new_dict[new]
print(old_dict)