#! /user/bin/python/
# -*-coding:utf-8 -*-

import tornado.web
container={}
dict
class Session():

    def __init__(self,handler):
        self.handler=handler
        self.random_str=""

    def getRandom_Str(self):
        """

        :return:  随机字符串
        """
        import time
        import hashlib
        obj=hashlib.md5()
        obj.update(bytes(str(time.time()),encoding='utf-8'))
        random_str=obj.hexdigest()
        return random_str
    def __getitem__(self, item):
        item_value=container.get(item,None)
        if not item_value:
            item_value=None
        return item_value
    def __setitem__(self, key, value):
        if not self.random_str:
            self.random_str=key
        if self.random_str not in container.keys():
            container[key]={}
        container[key]=value




class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session=Session(self)

class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        random_str=self.get_cookie("user_value",None)
        if random_str:
            value=self.session[random_str]
            if value:
                self.redirect('/manager')
            else:
                self.render('account/login.html')
        else:
            self.render('account/login.html')

    def post(self, *args, **kwargs):
        name=self.get_argument("name")
        pwd=self.get_argument("pwd")
        if name in ['alex','eric']:
            random_str=self.session.getRandom_Str()
            temp={"name":name,"pwd":pwd}
            self.session[random_str]=temp
            self.set_cookie("user_value",random_str)
            self.redirect('/manager')
        else:
            self.render('account/login.html')
class ManagerHandler(BaseHandler):
    def get(self, *args, **kwargs):
        random_str=self.get_cookie("user_value")
        if not random_str:
            self.redirect('/login')
        else:
            item=self.session[random_str]
            if not item:
                self.redirect('/login')
            else:
                name=item.get("name",None)
                self.render('account/manager.html',name=name)