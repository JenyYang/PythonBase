#! /user/bin/python/
# -*-coding:utf-8 -*-

import threading
import time

gl_sum=0
#创建线程锁对象
lock=threading.RLock()

def get_sum():
    #获取线程锁
    # lock.acquire()
    global gl_sum
    # time.sleep(1)
    gl_sum+=1
    print(gl_sum)
    #释放线程锁
    # lock.release()

for i in range(5):
    t=threading.Thread(target=get_sum)
    t.start()