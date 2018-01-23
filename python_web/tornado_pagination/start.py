#! /user/bin/python/
# -*-coding:utf-8 -*-
import tornado.web
import tornado.ioloop
from controllers import home


setting = {
    "template_path":"views"
}
application = tornado.web.Application(
    [('/index/(?P<page>\d*)',home.HomeHandler)],**setting
)

if __name__=="__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()