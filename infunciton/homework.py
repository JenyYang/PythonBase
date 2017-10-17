#!/user/bin/pyhton/
# -*-coding:utf-8 -*-

"""
1、删除用户
2、修改密码
"""
def delUser(username,password):
    f=open("user","r+",encoding="utf-8")
    for line in f:
        line= line.strip()
        line_list=line.split("$")
        print(line_list)
        # if username==line_list[0] and password==line_list[1]:
        #    return

def updatePwd(username,password,new_password):
    f=open("user","r+",encoding="utf-8")
    for line in f:
        line_temp=line
        line_list=line.strip().split("$")
        print(line_list)
        if username==line_list[0] and password==line_list[1]:
            print(line)
            line=line.replace(line_list[1],new_password)
            f.flush()
# delUser("yang","admin")
updatePwd("yang","admin","newadmin")