#! /user/bin/python/
# -*-coding:utf-8 -*-

"""
内置函数
"""
# abs 取绝对值

# all  循环参数 如果每个元素都为真，返回值为真 假（0，None，空值）

# any  循环参数 如果元素有一个为真 返回真

# ascii 参数传入对象  将会执行对象类中的 _repr_ 方法 获取其返回值

# bin  二进制

# hex 十六进制

# oct 八进制

# int() 十进制

# bool 判断真假  把对象转换成bool值

"""
bytes:字节
bytearray:字节列表
"""

# chr:接受数字 找到ascii码对应的字符  ord：接受字符 返回对应的ascii码   练习随机验证码

# callable

# divmod 得到商和余数的元组  项目分页使用

# eval 有返回值
a = "1+4"
i = eval(a)
print(i)
# exec   执行复杂的代码 没有返回值
exec("for i in range(10): print(i)")

#filter 根据提供的函数筛选可迭代的数据中符合条件的元素 filter(函数，可迭代的数据) 返回符合条件元素的集合 map
#map  map(函数，可迭代的对象)

#hash 获取指定对象的hash值  用于字典的优化

#iter 迭代器 创建一个可迭代的对象 next逐个取值

#pow 求指数

#zip

#sorted 排序 排序的数据只能是同一种类型的数据

#open  文件操作


