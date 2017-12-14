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
    with open("f.png","rb") as f:
        for line in f:
            conn.sendall(line)
    break

sk.close()

