from importlib import reload

from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from server.app import PyWebService
import six
reload(six)


if __name__ == '__main__':
    soap_app = Application([PyWebService], 'PyWebService',
                           in_protocol=Soap11(validator='lxml'),
                           out_protocol=Soap11())
    wsgi_app = WsgiApplication(soap_app)

    host = "127.0.0.1"
    port = 9567
    server = make_server(host, port, wsgi_app)
    print('WebService Started')
    print('http://' + host + ':' + str(port) + '/PyWebService/?wsdl')
    server.serve_forever()
