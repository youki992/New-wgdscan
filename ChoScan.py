#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:wgdScan
Author:wanggangdan
Copyright (c) 2019
'''
import sys
from lib.core.Spider import SpiderMain
import os
from script import printColor
import socket

def spider():
    pc.print_yellow_text('请输入URL（用单引号包含）：')
    root = str(input())
    root = root.replace('\'', '')
    threadNum = 10
    #spider
    wgd = SpiderMain(root, threadNum)
    wgd.craw()

def portscan(ip,port):
    #portscan
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False

def scan(ip, port):
    for x in port:
        r = portscan(ip, x)
        if r:
            pc.print_green_text('%s:%s is open' % (ip, x))
        else:
            print('%s:%s is close' % (ip, x))

def scan_start():
    pc.print_yellow_text('请输入服务器IP地址：')
    ip = str(input())
    port = [21, 22, 23, 80, 389, 873, 1433, 1521, 2049, 2181, 3306, 3389, 4848, 5900, 6379, 7001, 8080, 8089, 11211, 27017]
    scan(ip, port)

def xray(ip):
    os.chdir("./tools")
    exp=(("xray_windows_amd64.exe webscan --basic-crawler {0}").format(ip))
    pc.print_yellow_text('\nxray starting----------------------')
    os.system(exp)
    os.chdir("../")

def xray_start():
    with open('ip.txt','r') as file: list = [www.strip() for www in file.readlines()]
    for ip in list: xray(ip)

def SecurityMana():
    os.chdir("./tools")
    exp = ("Securityguards.exe")
    os.system(exp)
    os.chdir("../")

def default():
    pc.print_yellow_text('无此功能，请重新运行脚本！')
    quit()

def exit_r():
    exit()
switch = {'1' : spider,
          '2' : scan_start,
          '3' : xray_start,
          '4' : SecurityMana,
          '5' : exit_r}

if __name__ == '__main__':
    pc = printColor.Colors()
    pc.print_yellow_text('''
      ___ _          ____                  
     / __| |__   ___/ ___|  ___ __ _ _ __  
    / / _|  _ \ / _ \___ \ / __/ _  |  _ \ 
    | |_|| | | | (_) |__) | (_| (_| | | | |
    \ ___|_| |_|\___/____/ \___\__\_|_| |_|
                                   By:ch0bits
                                   Data:2021.04.07
            ''')
    while(1):
        pc.print_yellow_text('\n请输入数字 \n1 - 简单目录爬取 , \n2 - 扫描开放端口 ， \n3 - 调用xray扫描(请先在ip.txt中写入url) ， \n4 - 调用本地安全管理工具 , \n5 - 退出\n')
        num=str(input())
        switch.get(num,default)()