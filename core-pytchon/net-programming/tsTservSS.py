# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 9:55
# @Author  : JacobZhou

# SocketServer TCP服务器

from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from: ', self.client_address)
        s = '[%s] %s' % (ctime(), self.rfile.readline())
        self.wfile.write(bytes(s, 'utf-8'))


tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()
