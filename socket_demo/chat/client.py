#! /user/bin/python/
# -*-coding:utf-8 -*-

import socket

port=("127.0.0.1",9001)

sk=socket.socket()
sk.connect(port)


while True:
    data = sk.recv(1024)
    print(data)
    inp=raw_input("输入内容：")
    sk.sendall(str(inp))
    if inp=="q":
        break

sk.close()