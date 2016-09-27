#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
File Name: example-06.py
Description: 
Created_Time: 2016-09-27 14:52:22
Last modified: 2016-09-27 14时56分25秒
'''

_author = 'arron'
_email = 'fsxchen@gmail.com'


# Futrue, 类似于Promise和Deffer

import asyncio

@asyncio.coroutine
def slow_operation(future):
    yield from asyncio.sleep(1)
    future.set_result('Future is done!')

def got_result(future):
    print(future.result())
    loop.stop()

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
future.add_done_callback(got_result)
print("hello")
try:
    loop.run_forever()
finally:
    loop.close()
