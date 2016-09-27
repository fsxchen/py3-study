#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
File Name: example-04.py
Description: 
Created_Time: 2016-09-27 14:26:39
Last modified: 2016-09-27 14时29分42秒
'''

_author = 'arron'
_email = 'fsxchen@gmail.com'

# 协同程序
# 使用async def 来定义
# 或者是使用@asyncio.coroutine

import asyncio
import datetime

async def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(display_date(loop))
loop.close()
