#! /user/bin/python/
# -*-coding:utf-8 -*-

from wsgiref.simple_server import make_server

def RunServer(environ,start_response):
    start_response(status="200 0K",headers=[('Content-Type','text/html')])
    url=environ["PATH_INFO"]
    return "yangruijing"

if __name__=="__main__":
    httpd=make_server("",8000,RunServer)
    print("Serving http on 8000 port")
    httpd.serve_forever()

