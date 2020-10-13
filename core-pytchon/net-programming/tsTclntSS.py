# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 10:04
# @Author  : JacobZhou

# SocketServer TCP客户端

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    s = '%s\r\n' % data
    tcpCliSock.send(bytes(s, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.strip())
    tcpCliSock.close()
