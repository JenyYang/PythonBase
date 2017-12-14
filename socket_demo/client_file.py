#! /user/bin/python/
# -*-coding:utf-8 -*-

import socket

in_port=("127.0.0.1",9000)

sk=socket.socket()
sk.connect(in_port)
sk.close()