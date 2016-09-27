#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
File Name: example-03.py
Description: 
Created_Time: 2016-09-27 14:20:27
Last modified: 2016-09-27 14时26分14秒
'''

_author = 'arron'
_email = 'fsxchen@gmail.com'

# 事件循环

# asyncio.get_event_loop(), 返回一个loop
# asyncio.set_event_loop(loop), 设置

# 在不同的操作系统平台，可以使用的loop是不同的

import asyncio, sys

if sys.platform == 'win32':
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)

import selectors
selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)


