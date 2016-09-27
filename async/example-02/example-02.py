#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
File Name: example-02.py
Description: 
Created_Time: 2016-09-27 11:30:57
Last modified: 2016-09-27 14时18分33秒
'''

_author = 'arron'
_email = 'fsxchen@gmail.com'

# Futures，类似于Defer和Promise
# Tasks，使用future封装，返回一个Task的对象


# 例子： 监控文件的改变。



import asyncio
try:
    from socket import socketpair
except ImportError:
    from asyncio.windows_utils import socketpair

# Create a pair of connected file descriptors
rsock, wsock = socketpair()
loop = asyncio.get_event_loop()

def reader():
    data = rsock.recv(100)
    print("Received:", data.decode())
    # We are done: unregister the file descriptor
    loop.remove_reader(rsock)
    # Stop the event loop
    loop.stop()

# Register the file descriptor for read event
loop.add_reader(rsock, reader)

# Simulate the reception of data from the network
loop.call_soon(wsock.send, 'abc'.encode())

# Run the event loop
loop.run_forever()

# We are done, close sockets and the event loop
rsock.close()
wsock.close()
loop.close()

# import sys

# filename = sys.argv[1]

# loop = asyncio.get_event_loop()

# fd = open(filename, mode='rw')
# print(fd, "xx")

# def reader():
#     print("readding")

# loop.add_reader(fd, reader)

# loop.run_forever()

# fd.close()
# loop.close()
