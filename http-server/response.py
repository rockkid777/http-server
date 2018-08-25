from status import Status

class Response:

    def __init__(self, status = Status.Ok(), headers = {}, body = ''
                , httpVer = "HTTP/1.1"):
        self.status = status
        self.headers = headers
        self.body = body
        self.httpVer = httpVer

    def toString(self):
        headersArr = []
        for k, v in self.headers.iteritems() :
            headersArr.append("{}: {}".format(k, v))
        headersStr = "\r\n".join(headersArr)
        return "\r\n".join(["{} {}".format(self.httpVer, self.status.toString())
                            , headersStr
                            , ''
                            , str(self.body)])
