# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 10:19
# @Author  : JacobZhou

# Twisted Reactor TCP 服务器

from time import ctime

from twisted.internet import protocol, reactor

PORT = 21567


class TSServProtocal(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from: ', clnt)

    def dataReceived(self, data):
        s = '[%s] %s' % (ctime(), data)
        self.transport.write(bytes(s, 'utf-8'))


factory = protocol.Factory()
factory.protocol = TSServProtocal
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()
