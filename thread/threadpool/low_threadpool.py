#! /user/bin/python/
# -*-coding:utf-8 -*-
import threading,queue
class ThreadPool(object):
    def __init__(self,maxnum):
        self.maxnum=maxnum
        self.q=queue.Queue(self.maxnum)
        for i in range(self.maxnum):
            self.q.put(threading.Thread)
    def get_q(self):
        return self.q.get()

    def add_thread(self,thread):
        self.q.put(thread)

def fuac(args,pool):
    print(args)
    import time
    time.sleep(0.5)
    pool.add_thread(threading.Thread)



# if __name__=="__main":

pool=ThreadPool(5)

for i in range(100):
    q = pool.get_q()
    t=q(target=fuac,args=(i,pool))
    t.start()
