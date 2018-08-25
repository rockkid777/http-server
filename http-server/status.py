class Status:

    def __init__(self, code = 200, msg = "OK"):
        self.code = code
        self.msg = msg

    def toString(self, separator = " "):
        return separator.join([str(self.code), self.msg])

    @staticmethod
    def Continue():
        return Status(100, "Continue")

    @staticmethod
    def SwitchingProtocols():
        return Status(101, "Switching Protocols")

    @staticmethod
    def Ok():
        return Status(200, "OK")

    @staticmethod
    def Created():
        return Status(201, "Created")

    @staticmethod
    def Accepted():
        return Status(202, "Accepted")

    @staticmethod
    def NonAuthoritiveInformation():
        return Status(203, "Non-Authoritive Information")

    @staticmethod
    def NoContent():
        return Status(204, "No Content")

    @staticmethod
    def ResetContent():
        return Status(205, "Reset Content")

    @staticmethod
    def PartialContent():
        return Status(206, "Partial Content")

    @staticmethod
    def MultipleChoices():
        return Status(300, "Multiple Choices")

    @staticmethod
    def MovedPermanently():
        return Status(301, "Moved Permanently")

    @staticmethod
    def Found():
        return Status(302, "Found")

    @staticmethod
    def SeeOther():
        return Status(303, "See Other")

    @staticmethod
    def NotModified():
        return Status(304, "Not Modified")

    @staticmethod
    def UseProxy():
        return Status(305, "Use Proxy")

    @staticmethod
    def TemporaryRedirect():
        return Status(307, "Temporary Redirect")

    @staticmethod
    def BadRequest():
        return Status(400, "Bad Request")

    @staticmethod
    def Unauthorized():
        return Status(401, "Unauthorized")

    @staticmethod
    def PaymentRequired():
        return Status(402, "Payment Required")

    @staticmethod
    def Forbidden():
        return Status(403, "Forbidden")

    @staticmethod
    def NotFound():
        return Status(404, "Not Found")

    @staticmethod
    def MethodNotAllowed():
        return Status(405, "Method Not Allowed")

    @staticmethod
    def NotAcceptable():
        return Status(406, "Not Acceptable")

    @staticmethod
    def ProxyAuthenticationRequired():
        return Status(407, "Proxy Authentication Required")

    @staticmethod
    def RequestTimeout():
        return Status(408, "Request Time-out")

    @staticmethod
    def Conflict():
        return Status(409, "Conflict")

    @staticmethod
    def Gone():
        return Status(410, "Gone")

    @staticmethod
    def LengthRequired():
        return Status(411, "Length Required")

    @staticmethod
    def PreconditionFailed():
        return Status(412, "Precondition Failed")

    @staticmethod
    def RequestEntityTooLarge():
        return Status(413, "Request Entity Too Large")

    @staticmethod
    def RequestURITooLarge():
        return Status(414, "Request-URI Too Large")

    @staticmethod
    def UnsupportedMediaType():
        return Status(415, "Unsupported Media Type")

    @staticmethod
    def Requestedrangenotsatisfiable():
        return Status(416, "Requested range not satisfiable")

    @staticmethod
    def ExpectationFailed():
        return Status(417, "Expectation Failed")

    @staticmethod
    def InternalServerError():
        return Status(500, "Internal Server Error")

    @staticmethod
    def NotImplemented():
        return Status(501, "Not Implemented")

    @staticmethod
    def BadGateway():
        return Status(502, "Bad Gateway")

    @staticmethod
    def ServiceUnavailable():
        return Status(503, "Service Unavailable")

    @staticmethod
    def GatewayTimeout():
        return Status(504, "Gateway Time-out")

    @staticmethod
    def HTTPVersionnotsupported():
        return Status(505, "HTTP Version not supported")
