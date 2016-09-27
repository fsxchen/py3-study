#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
File Name: portscan.py
Description: 
Created_Time: 2016-09-27 15:43:51
Last modified: 2016-09-27 20时08分07秒
'''

_author = 'arron'
_email = 'fsxchen@gmail.com'

import asyncio
import socket
# import requests


PORTS=[21, 22, 23, 80, 110, 143, 443, 445, 3306, 3389, 6379, 27017, 8000, 8080]

@asyncio.coroutine
def port_scan(ip, port):
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((ip, port))
        print("ip %s port %d is open!" % (ip, port))
        # if port == 80:
            
        #     banner = s.recv(1024)
        # else:
        #     bannser = s.recv(1024)
        # print(banner)
    except Exception as e:
        pass


def main():
    loop = asyncio.get_event_loop()
    tasks = []
    import sys
    ip = sys.argv[1]
    for port in PORTS:
        tasks.append(asyncio.ensure_future(port_scan(ip, port)))
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

if __name__ == "__main__":
    main()
