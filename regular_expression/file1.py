#! /user/bin/python/
# -*-coding:utf-8 -*-
import re

# findall(匹配规则，匹配内容) 将所有符合规则的字符串以列表的形式返回
ret = re.findall("yang", "jfljdlyangklkyangjljoyang")
print(ret)
"""
元字符：.(点)：通配符 换行符以外的任何字符（仅代表一个字符）
        ^(尖角符)：匹配规则必须在开头 在字符集中是非的意思 例如：[^1-9] 除了数字以外的字符
        $:控制末尾（匹配规则必须在末尾）
        *：前面紧挨着的字符出现0到多次
        +：前面紧挨着的字符出现一到多次
        ？：前面紧挨着的字符出现0-1次
        {数字}：控制出现的次数{数字，数字}是一个闭区间
        []:字符集 里面的字符中任何一个存在（只有一个）就匹配 通配符符在字符集中只是一个普通字符
        -：在字符集中有 从头到尾连接的意思 例如：1-9
        \：后加元字符 元字符去除特殊功能  后加普通字符赋予特殊功能
        \d：任何十进制数 \D：任何非数字字符==[^1-9] \s：任何空白字符==[\t\n\r\f\v]
        \S:任何非空白字符  \w： 任何字母数字字符==[a-zA-Z0-9]
        \W:任何非字母数字字符 \b:一个单词边界 也就是指单词和空格间的位置
        ():组 将里面的内容作为一个整体匹配
        +，*后面加？：表示原来意义上取最小的 例如：  （\d+）:贪婪模式 多个十进制数字  (\d+?)：非贪婪模式 一个十进制数字 
        如果组的前后都有其他字符将整个组夹着，既是添加了？也不走非贪婪
        \数字:引用序号对应的组所匹配的字符串
        ?:  :在组中规则的前面添加?: 表示取消优先匹配组的权限
        
    
        
        
"""
# search 找到一个符合规则的就结束
re.search("yang", "abyang").group()
# metch 只匹配开头的内容 没有结果默认none 有结果 得到的是一个match对象
# re.match()

ret = re.findall(r"a(\d+?)", "sda234323b")
print(ret)
"""
re.I:使匹配对大小写不敏感
"""
ret = re.search("com", "COM", re.I).group()
print(ret)
# re.S 将.（点）把换行符包含在内
ret = re.findall(".", "afsdgfs\nsd", re.S)
print(ret)

# re.sub() 替换指定的子串
s = "aabbaabbaabbab"
s1 = re.sub("bb", "cc", s, 2)
print(s1)
# re.compile(规则) 将规则编译成对象  适用于多次使用一个规则匹配 这样每次匹配时就可以直接使用编译的对象
p = re.compile("\d+")
s = "one1two2three"
ret = p.split(s)
print(ret)


# 乘号匹配
def search_multiple(args):
    result = re.search("\d+\.?\d*([*/]|\*\*)\d+\.?\d*").group()
    return result


# 加好匹配
def regular_add(args):
    result = re.search("\d+\.?\d*[\+\-]\d+", args).group()
    return result


# 加号处理
def operation_add(args):
    sum = 0
    add_list = args.split("+")
    print(add_list)
    for i in add_list:
        if i.find(".") != -1:  # 浮点型计算
            print("执行了")
            sum += float(i)
        else:  # 整型计算
             sum += int(i)
        print(sum)
    return sum


s = "5 * (4 + (-3 * 2 + 6 / 3 + (5+5-3) * 2)) - 8"
ret1 = re.search("\([^()]*\)", s).group()
print(ret1)
while ret1:
    result = regular_add(ret1)
    print(result)
    if result:
        n=operation_add(result)
        print(n)
        ret1 = ret1.replace(result, str(n))
    print(ret1)
