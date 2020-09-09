#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:wgdScan
Author:wanggangdan
Copyright (c) 2019
'''
import sys
from lib.core.Spider import SpiderMain
def main():
    print('请输入URL（用单引号包含）：', end='')
    root = str(input())
    root = root.replace('\'', '')
    threadNum = 10
    #spider
    wgd = SpiderMain(root, threadNum)
    wgd.craw()

if __name__ == '__main__':
    main()