import sys
import socket
import request

port = int(sys.argv[1] if len(sys.argv) > 1 else 8080)
print("Running on port {}".format(port))

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind(('', port))
listen_socket.listen(1)

while True:
    connection, client_address, = listen_socket.accept()
    req = connection.recv(1024)
    httpRequest = request.Request.fromString(req)
    print(httpRequest)
    print(httpRequest.path)
    print(httpRequest.queryParams)
    print(httpRequest.headers)

    # print(req.split('\r\n'))
    body = '{"a":123}'

    http_response = """\
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: {}

{}""".format(len(body), body)
    print("------------")
    print(http_response)

    connection.sendall(http_response)
    connection.close()
