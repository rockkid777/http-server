import sys
import socket
from ..request import Request
from ..response import Response
from ..status import Status
from ..route import Route
from ..router import Router
from ..controller import Controller

class MyController(Controller) :
    def postEcho(self, request, response):
        response = Response(status = Status.Ok()
                          , body = request.body)

    def getEcho(self, request, response):
        msg = request.params["msg"]
        response.status = Status.Ok()
        response.body = {"msg": msg}

    def registerHandlers(self, router):
        router.addRoute("POST", "/echo", self.postEcho)
        router.addRoute("GET", "/echo/:msg", self.getEcho)

class MyRouter(Router):
    def registerControllers(self):
        self.controllers.append(MyController(self))

port = int(sys.argv[1] if len(sys.argv) > 1 else 8080)

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind(('', port))
listen_socket.listen(1)
print("Running on port {}".format(port))

router = MyRouter("/api/v1/")
router.registerControllers()
router.loadRoutes()

while True:
    connection, client_address, = listen_socket.accept()
    req = connection.recv(1024)
    httpRequest = Request.fromString(req)
    print(httpRequest)
    print(httpRequest.path)
    print(httpRequest.queryParams)
    print(httpRequest.headers)

    # print(req.split('\r\n'))
    # body = '{"a":123}'

    response = Response()
    router.route(httpRequest, response)

    print("------------")
    print(response.toString())

    connection.sendall(response.toString())
    connection.close()
