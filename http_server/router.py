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

    def addRoute(self, method, path, handler):
        if method == "GET" :
            routes = self.get
        elif method == "POST" :
            routes = self.post
        elif method == "PUT" :
            routes = self.put
        elif method == "PATCH" :
            routes = self.patch
        elif method == "DELETE" :
            routes = self.delete
        else :
            return
        route = Route(method, self.pathPrefix, path, handler)
        routes.append(route)

    def loadRoutes(self):
        for router in self.routers :
            router.loadRoutes()
        for controller in self.controllers :
            controller.registerHandlers(self)

    def _local_route(self, routes, request, response):
        for route in routes :
            m = route.regex.match(request.path)
            if m :
                request.params = m.groupdict()
                route.handler(request, response)
                return True
        return False

    def route(self, request, response = Response(status=Status.NotFound())):
        for router in self.routers :
            if router.route(request, response) :
                return True
        if request.method == "GET" :
            return self._local_route(self.get, request, response)
        if request.method == "POST" :
            return self._local_route(self.post, request, response)
        if request.method == "PUT" :
            return self._local_route(self.put, request, response)
        if request.method == "PATCH" :
            return self._local_route(self.patch, request, response)
        if request.method == "DELETE" :
            return self._local_route(self.delete, request, response)
        return False
