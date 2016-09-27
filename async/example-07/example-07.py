#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
File Name: example-07.py
Description: 
Created_Time: 2016-09-27 14:57:00
Last modified: 2016-09-27 15时08分05秒
'''

_author = 'arron'
_email = 'fsxchen@gmail.com'

# Tasks 并行的执行协程

import asyncio

@asyncio.coroutine
def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        # yield from asyncio.sleep(1)
        f *= i
    print("Task %s: factorial(%s) = %s" % (name, number, f))

loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(factorial("A", 2)),
    asyncio.ensure_future(factorial("B", 3)),
    asyncio.ensure_future(factorial("C", 4))]
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
