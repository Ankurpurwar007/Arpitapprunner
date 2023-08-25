from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os
import socket
import logging
port = int(os.environ.get("PORT"))
data = socket.gethostbyname_ex("www.google.com")
def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + str(port) + "!\n"
    logging.debug("\n\nThe IP Address of the Domain Name is: "+repr(data))
    return Response(message + "\n\nThe IP Address of the Domain Name is: "+repr(data))

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
