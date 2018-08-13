
def _parseQueryParams(queryString):
    params = queryString.split('&')
    valids = [a.split('=') for a in params if len(a.split('=')) == 2]
    queryParams = {}
    for pair in valids :
        queryParams[pair[0]] = pair[1]
    return queryParams

def _getPathAndQueryParams(fullPath):
    ind = fullPath.find('?')
    path = fullPath[:ind] if ind > -1 else fullPath
    queryParams = _parseQueryParams(fullPath[(ind + 1):]) if ind > -1 else {}
    return (path, queryParams)

def requestFromString(req):
    lines = req.split('\r\n')
    method, path, queryParams, httpVer = '', '', {}, ''
    args = lines[0].split(' ')
    method = args[0].upper()
    httpVer = args[2]
    (path, queryParams) = _getPathAndQueryParams(args[1])
    bodyStartInd = lines.index('')

    headers = {}
    for line in lines[1:bodyStartInd]:
        ind = line.find(':')
        if ind < 0 && ind < (len(line) - 1):
            continue
        key = line[:ind].strip()
        value = line[(ind + 1):].strip()
        headers[key] = value

    body = "\r\n".join(lines[(bodyStartInd + 1):]) if bodyStartInd > -1 else ""

    return Request(method, path, {}, queryParams, httpVer, headers, body)

class Request:
    """HTTP request"""

    def __init__(self, method="GET", path="/", params={}, queryParams={},
                 httpVer="", headers={}, body=""):
        self.method = method
        self.path = path
        self.params = params,
        self.queryParams = queryParams
        self.httpVer = httpVer
        self.headers = headers
        self.body = body
