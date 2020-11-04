# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 20:14
# @Author  : JacobZhou

from socket import *

HOST = 'localhost'
PORT = 50007
ADDR = (HOST, PORT)

echoCltSock = socket(AF_INET, SOCK_STREAM)
echoCltSock.connect(ADDR)

while True:
    data = input('> ')
    echoCltSock.sendall(bytes(data, 'utf-8'))
    recv = echoCltSock.recv(1024)
    print(str(recv, 'utf-8'))
