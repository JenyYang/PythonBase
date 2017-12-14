#! /user/bin/python/
# -*-coding:utf-8 -*-

import socket

port=("127.0.0.1",8055)

sk=socket.socket()
sk.connect(port)
ret=sk.recv(1024)
total_size=int(ret)
f=open("new.png","wb")
has_size=0
while True:
    line=sk.recv(1024)
    has_size+=len(line)
    f.write(line)
    if has_size==total_size:
        break

sk.close()