#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
File Name: hello_async.py
Description: 
Created_Time: 2016-09-27 11:13:06
Last modified: 2016-09-27 11时29分27秒
'''

# event loop 是核心，主要有一下的作用。

# 1. 注册，执行，取消执行以及延时调用。
# 2. 为服务端和客户端提供transport
# 3. 为子进程和其他进程通信提供transports
# 4. 线程池函数调用授权



# 例子，简单调用

_author = 'arron'
_email = 'fsxchen@gmail.com'
import asyncio

def floop1(loop):
    print('loop1')

def floop2(loop):
    print('loop2')

loop1 = asyncio.get_event_loop()
loop2 = asyncio.get_event_loop()

loop1.call_soon(floop1, loop1)
loop2.call_later(1, floop2, loop2)

loop1.run_forever()
loop2.run_forever()
loop1.close()
