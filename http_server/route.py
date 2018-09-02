import re

class Route:

    def __init__(self, method, pathPrefix, pathExp, controller, handler):
        self.method = method.upper()
        self.regex = re.compile(Route.makePathRegExp(pathPrefix, pathExp))
        self.controller = controller
        self.handler = handler

    @staticmethod
    def makePathRegExp(pathPrefix, pathExp):
        def conv(chunk):
            if len(chunk) < 2 or chunk[0] != ':' :
                return chunk
            name = chunk[1:]
            return "(?P<{}>[^/]+)".format(name)
        suffix = "/" if pathExp[-1] == "/" else ""
        exp = "/".join(map(conv, pathExp.split('/')[1:])) + suffix
        return "^" + pathPrefix + exp + "$"
