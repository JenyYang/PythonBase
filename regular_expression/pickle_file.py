#! /user/bin/python/
# -*-coding:utf-8 -*-
"""
 pickle序列化：
 pickle.loads(文件/字符串) 读取文件或字符串所有内容
 pickle.dumps(内容) 将指定内容转换成字符串
"""
import pickle

# dic={1:{"name":"yangruijing","password":"yangadmin","age":26,"gender":"女"}}
# print(dic)
account_file = open("account", "rb")
"""
读取有的时候会捕获到Ran out of input 原因是读取的指针超出了内容范围
"""
account_dict = pickle.loads(account_file.read())
account_file.close()
account_dict[1]["name"] = "ruijing"
waccount_file = open("account","wb")
waccount_file.write(pickle.dumps(account_dict))
waccount_file.close()
account_file = open("account", "rb")
account_dict = pickle.loads(account_file.read())
print(account_dict)
account_file.close()
