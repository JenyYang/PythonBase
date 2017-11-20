#! /user/bin/python/
# -*-coding:utf-8 -*-

"""
日志等级
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0

"""
# 单文件日志

# import logging
#
# logging.basicConfig(filename='log.log',
#                     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',
#                     level=10)
#
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
# logging.log(10, 'log')
# logging.basicConfig(filename="log.log", format='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p', level=logging.DEBUG)
# logging.debug("debug")
# logging.error("error")
# logging.warning("warn")
# logging.critical("critical")
# logging.info("info")
# logging.log(10,"log")


#多文件日志

import logging

""""
多文件日志 basicConfig无法完成 需要自定义文件和日志操作对象
步骤：
    1、定义文件
    2、定义日志格式
    3、将日志格式设置给文件对象
    4、定义日志
    5、将文件对象添加到定义的日志中
    6、写日志
"""
#定义文件1
file_l1=logging.FileHandler("log_l1.log","a")
#定义日志格式
file_format=logging.Formatter(fmt="%(asctime)s-%(name)s-%(levelname)s-%(module)s: %(message)s")
#设置日志格式
file_l1.setFormatter(file_format)

#定义文件2
file_l2=logging.FileHandler("log_l2.log","a")
file_l2.setFormatter(file_format)

#定义日志

log=logging.Logger("s1",logging.DEBUG)

#添加日志文件对象
log.addHandler(file_l1)
log.addHandler(file_l2)

#写日志
log.critical("最高级")

