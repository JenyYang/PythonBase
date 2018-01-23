#! /user/bin/python/
# -*-coding:utf-8 -*-

import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        cok=self.get_cookie("auto")
        if cok=="1":
            self.redirect("/mine")
        else:
            self.render("login.html",status="")
    def post(self, *args, **kwargs):
        username=self.get_argument("name")
        pwd=self.get_argument("pwd")
        if username=="alex" and pwd=="alex":
            self.set_cookie("auto","1")
            self.redirect("/mine")
        else:
            self.render("login.html",status="用户名或密码错误")
class LoginOutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie("auto","")
        self.redirect("/login")
class MineHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("mine.html")

setting={
    "template_path":"template",
}

#路由映射
application = tornado.web.Application([("/index",IndexHandler)
                                       ,("/login",LoginHandler)
                                       ,("/mine",MineHandler)
                                       ,("/loginout",LoginOutHandler)],**setting)

if __name__=="__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
