#! /user/bin/python/
# -*-coding:utf-8 -*-

from wsgiref.simple_server import make_server
def index():
    return 'index'
def new():
    return 'new'
def info():
    return 'info'

URLS={'/index':index,'/new':new,'/info':info}


def RunServer(environ,start_response):
    start_response('200 0K',[('Content-Type','text/html')])
    url=environ['PATH_INFO']
    if url in URLS.keys():
        fuac_name=URLS[url]
        ret = fuac_name()
    else:
        ret="404"
    return ret
if __name__=="__main__":
    httpd=make_server('',8000,RunServer)
    httpd.serve_forever()