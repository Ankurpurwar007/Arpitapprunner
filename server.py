from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os
import socket
import logging
port = int(os.environ.get("PORT"))
i = 0
def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + str(port) + "!\n"
    data = socket.gethostbyname_ex("www.google.com")
    logging.debug("\n\nThe IP Address of the Domain Name is: "+repr(data))
    i += 1
    return Response(message + "\n\nThe IP Address of the Domain Name is: "+repr(data) + i)
    

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
