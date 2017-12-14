#! /user/bin/python/
# -*-coding:utf-8 -*-

import socket

port = ("127.0.0.1", 9001)

sk = socket.socket()
sk.bind(port)
sk.listen(10)

while True:
    conn, addr = sk.accept()
    conn.sendall("欢迎来到聊天室")
    data = conn.recv(1024)
    while data:
        # data_str=str(data,encoding="utf-8")
        if data == "q":
            break
        print(data)
        inp = raw_input("输入内容：")
        conn.sendall(inp)
        data = conn.recv(1024)

sk.close()
