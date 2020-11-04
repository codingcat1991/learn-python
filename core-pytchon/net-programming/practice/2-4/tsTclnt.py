# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 12:42
# @Author  : JacobZhou

# TCP客户端

from socket import *

HOST = input('请输入主机IP(默认localhost)：') or 'localhost'
PORT = int(input('请输入端口号（默认21567）：') or '21567')
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()
