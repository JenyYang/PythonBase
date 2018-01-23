#! /user/bin/python/
# -*-coding:utf-8 -*-

import tornado.web

import tornado.ioloop
import uimethods as mt
import uimodule as md
USER_LIST=[]
class MyRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("s1.html",user_list=USER_LIST)
    def post(self, *args, **kwargs):
        print("post")
        user=self.get_argument("username")
        USER_LIST.append(user)
        self.render("s1.html",user_list=USER_LIST)

settings={
    "template_path":"template",
    "static_path":"static",
    "ui_methods":mt,
    "ui_modules":md

}
application=tornado.web.Application([(r'/index',MyRequestHandler)],**settings)
if __name__=="__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()