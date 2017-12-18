#! /user/bin/python/
# -*-coding:utf-8 -*-

import SocketServer


class MyHandle(SocketServer.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall("欢迎来电")
        while True:
            data = conn.recv(1024)
            print(data)
            if data=="q":
                break
            inp=raw_input("请输入")
            conn.sendall(inp)
        conn.close()

if __name__=="__main__":
    server=SocketServer.ThreadingTCPServer(("127.0.0.1",8001),MyHandle)
    server.serve_forever()