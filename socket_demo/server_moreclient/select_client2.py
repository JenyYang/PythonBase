#! /user/bin/python/
# -*-coding:utf-8 -*-

import socket

port = ("127.0.0.1", 8002)

sk = socket.socket()
sk.connect(port)
# welcome=sk.recv(1024)
# print(welcome)
while True:
    data = sk.recv(1024)
    print(data)
    inp = raw_input("请输入")
    sk.sendall(inp)
    if inp == "q":
        break
sk.close()
