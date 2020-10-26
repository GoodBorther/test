#!/usr/bin/python3
#-*- coding: utf-8 -*-
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 4444))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
l = [b'\xe5\xb0\x8f\xe5\xad\x9f',b'asd',b'asd']
for data in l:
        # 发送数据:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
