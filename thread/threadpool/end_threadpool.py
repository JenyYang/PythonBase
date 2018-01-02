#! /user/bin/python/
# -*-coding:utf-8 -*-

import threading,queue

import time

#线程终止标记
StopEvent=object()

class ThreadPool(object):
    def __init__(self,maxnum):
        self.maxnum=maxnum
        self.q=queue.Queue()
        self.free_list=[]
        self.generate_list=[]
        self.terminal=False

    def run(self,fuac,args,callback=None):
        """

        :param fuac: 任务函数
        :param args: 任务参数
        :param callback: 回调函数
        :return:
        """
        #判断是否符合创建线程的条件
        if len(self.free_list)==0 and len(self.generate_list)<self.maxnum:
            self.generate_thread()
        #将任务封装成任务包（元祖）
        w=(fuac,args,callback)
        #将任务包添加到任务队列
        self.q.put(w)

    def generate_thread(self):
        """
        创建线程
        :return:
        """
        t=threading.Thread(target=self.call)
        t.start()

    def call(self):
        """
        循环获取任务并执行任务
        :return:
        """
        #获取当前线程，并添加到生成线程列表中
        t=threading.currentThread
        self.generate_list.append(t)
        #获取任务
        event=self.q.get()

        while event != StopEvent:
            #执行任务
            fuac,args,callback=event

            #调用任务函数
            try:
                fuac(args)
            except Exception as e:
                pass
            #任务完成，线程空闲
            self.free_list.append(t)
            #获取新任务
            event=self.q.get()
            #线程繁忙
            self.free_list.remove(t)

        else:
            #线程终止，生成线程列表中移除该线程
            self.generate_list.remove(t)
    def close(self):
        while len(self.generate_list):
            self.q.put(StopEvent)

def action(args):
    time.sleep(0.5)
    print(args)

pool=ThreadPool(10)

for i in range(100):
    pool.run(action,i)

pool.close()


