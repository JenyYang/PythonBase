#! /user/bin/python/
# -*-coding:utf-8 -*-

from tornado.web import UIModule

class Comment(UIModule):
    def render(self, *args, **kwargs):
        return "UIMODULE"