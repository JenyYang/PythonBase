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
        ret={"status":"","message":""}
        if username=="alex" and pwd=="alex":
            self.set_cookie("auto","1")
            ret["status"]="200"
            ret["message"]="ok"
            # self.redirect("/mine")
        else:
            ret["status"] = "401"
            ret["message"] = "fail"
        self.write(ret)
class LoginOutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie("auto","")
        self.redirect("/login")
class MineHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("mine.html")

setting={
    "template_path":"template",
    "static_path":"static"
}

#路由映射
application = tornado.web.Application([("/index",IndexHandler)
                                       ,("/login",LoginHandler)
                                       ,("/mine",MineHandler)
                                       ,("/loginout",LoginOutHandler)],**setting)

if __name__=="__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
