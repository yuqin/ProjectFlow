# coding: utf-8


###############################sample1################################

from time import sleep, ctime 
import threading
import os
import sys
import time
import subprocess
import re



def getDeviceName():
    deviceName=subprocess.getoutput('adb devices').split("\n")[1].split("\t")[0] 
    return  deviceName


# if __name__ == '__main__':
#     #启动线程
#     for i in files:
        
#         threads[i].start()
#     for i in files:
#         threads[i].join()
 
#     #主线程
#     print 'end:%s' %ctime()


# 目前的简单操作如下
os.system("adb -s 9YJNW17719006863 shell input tap 275 122") #打开小红书 
os.system("adb -s 9YJNW17719006863 shell input tap 360 1254") #回到主菜单
os.system("adb -s 9YJNW17719006863 shell input tap 670 108") #打开右上搜索
os.system("adb -s 9YJNW17719006863 shell input text {lisa}") #寻找特定的内容
os.system("adb -s 9YJNW17719006863 shell input tap 260 837") #寻第一条内容点赞
os.system("adb -s 9YJNW17719006863 shell input tap 52 111") #回退
#adb -s 9YJNW17719006863 shell input text {text}

#后续可以根据需求 添加进程及工作台