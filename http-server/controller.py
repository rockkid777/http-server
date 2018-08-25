from request import Request
from response import Response
from status import Status

class Controller:

    def __init__(self, router = None):
        self.router = router

    def registerHandlers(self, router = self.router):
        # for override
        pass
