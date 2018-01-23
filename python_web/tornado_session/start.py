#! /user/bin/python/
# -*-coding:utf-8 -*-
import tornado.web
import tornado.ioloop
from controllers import account


setting = {
    "template_path":"views"
}
application = tornado.web.Application(
    [
        ('/login',account.LoginHandler),
        ('/manager',account.ManagerHandler)
     ],**setting
)

if __name__=="__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()