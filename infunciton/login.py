#!/user/bin/pyhton/
# -*-coding:utf-8 -*-

#登录方法
def tologin(username,password):
    """
    :param username: 用户名
    :param password: 密码
    :return:  True 登录成功 Flase 登录失败
    """
    file=open("user","r",encoding="utf-8")
    for line in file:
        line=line.strip()
        line_list=line.split("$")
        if username==line_list[0] and password==line_list[1]:
            return True
    return False
name=input("请输入用户名:")
pwd=input("请输入密码:")
flag=tologin(name,pwd)
if flag:
    print("登录成功")
else:
    print("登录失败")

# def toregister(username,password):
#
