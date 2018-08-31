from request import Request
from response import Response
from status import Status
from route import Route

class Router:

    def __init__(self, pathPrefix='', routers=[]):
        self.pathPrefix = pathPrefix
        self.routers = routers
        self.controllers = []
        self.get = []
        self.post = []
        self.put = []
        self.patch = []
        self.delete = []

    def registerControllers(self):
        # for override
        pass

    def loadRoutes(self):
        for router in routers :
            router.loadRoutes()
        for controller in controllers :
            controller.registerHandlers(self)

    def _local_route(self, routes, request, response):
        for route in routes :
            if route.match(request.path) :
                route.handler(request, response)
                return True
        return False

    def route(self, request, response = Response().NotFound):
        for router in routers :
            if router.route(request, response) :
                return True
        if request.method == "GET" :
            return _local_route(self.get, request, response)
        if request.method == "POST" :
            return _local_route(self.post, request, response)
        if request.method == "PUT" :
            return _local_route(self.put, request, response)
        if request.method == "PATCH" :
            return _local_route(self.patch, request, response)
        if request.method == "DELETE" :
            return _local_route(self.delete, request, response)
        return False
