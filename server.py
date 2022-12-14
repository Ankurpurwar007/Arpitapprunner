from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import requests

import os

def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + "!\n"
    response1 = requests.get("https://r2xqadrzpk.us-east-2.awsapprunner.com/api/user/users")
    print(response1.text)
    print(message)
    response2 = requests.get("https://unhaw3wrck.us-east-2.awsapprunner.com/api/user/users")
    print(response2.text)
    print(message)
    return Response(message + response1.text + response2.text)
    

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
