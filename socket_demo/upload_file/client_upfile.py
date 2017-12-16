#! /user/bin/python/
# -*-coding:utf-8 -*-

import socket
import os

port=("127.0.0.1",8055)

sk=socket.socket()
sk.bind(port)
sk.listen(10)

while True:
    conn,addr=sk.accept()
    total_size =os.stat("f.png").st_size
    conn.sendall(str(total_size))
    #发送文件大小和文件正文中间进行一次接受操作，解决数据粘包问题 原理：发送完一次内容后，服务端不
    #返回数据即接受不到返回内容不会进行下次发送操作
    conn.recv(1024)
    with open("f.png","rb") as f:
        for line in f:
            conn.sendall(line)
    break

sk.close()

