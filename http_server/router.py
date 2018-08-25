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

    def route(self, request, response = Response()):
        #todo
        pass
