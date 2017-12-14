#! /user/bin/python/
# -*-coding:utf-8 -*-

import socket

in_port = ("127.0.0.1", 9000)

sk = socket.socket()
sk.bind(in_port)
sk.listen(5)
while True:
    conn, addr = sk.accept()
    print(addr,conn)
sk.close()
