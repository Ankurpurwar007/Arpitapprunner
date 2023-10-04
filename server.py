from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os
import socket
import logging
port = int(os.environ.get("PORT"))
def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + str(port) + "!\n"
    data = socket.gethostbyname_ex("www.google.com")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.google.com', 80))
    request = b'HEAD google.com HTTP/1.1\n\n'
    s.send(request)
    print(s.recv(4096).decode())
    logging.debug("\n\nThe IP Address of the Domain Name is: "+repr(data))
    return Response(message + "\n\nThe IP Address of the Domain Name is: "+repr(data) + "\n final" +s.recv(4096).decode())
    

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
