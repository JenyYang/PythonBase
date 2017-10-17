#! /user/bin/python/
# -*-coding:utf-8 -*-
"""

/r 每一次清空
"""
import sys
import time

for i in range(31):
    sys.stdout.write("\r") #每次清空
    sys.stdout.write("%s %% | %s" % (int(i/30*100),i*"*"))
    sys.stdout.flush()
    time.sleep(0.2)