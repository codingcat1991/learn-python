# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 19:27
# @Author  : JacobZhou

# UDP服务端

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    s = '[%s] %s' % (ctime(), data)
    udpSerSock.sendto(bytes(s, 'utf-8'), addr)
    print('...received from and returned to: ', addr)

udpSerSock.close()
