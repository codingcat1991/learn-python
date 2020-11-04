# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 19:22
# @Author  : JacobZhou
import os
from socket import *
from time import ctime

HOST = ''
PORT = 50007
ADDR = (HOST, PORT)

echoSerSock = socket(AF_INET, SOCK_STREAM)
echoSerSock.bind(ADDR)
echoSerSock.listen(1)
while True:
    conn, addr = echoSerSock.accept()
    print('Connected by ', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        if data == b'date':
            conn.sendall(bytes(ctime(), 'utf-8'))
        elif data == b'os':
            conn.sendall(bytes(os.name, 'utf-8'))
        elif data == b"ls":
            conn.sendall(bytes('\n'.join(os.listdir()), 'utf-8'))
        elif data.startswith(b'ls '):
            path = data.split(b' ')[1]
            try:
                conn.sendall(bytes('\n'.join(os.listdir(str(path, 'utf-8'))), 'utf-8'))
            except:
                conn.sendall(bytes('不存在此目录', 'utf-8'))
        else:
            conn.sendall(bytes('请输入正确的命令', 'utf-8'))
    conn.close()
