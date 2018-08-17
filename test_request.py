import unittest
from request import Request


class TestRequestParsing(unittest.TestCase):

    def setUp(self):
        self.simpleStrGetRequest = "\r\n".join([
              "GET /hello/ginger?a=123 HTTP/1.1"
            , "Host: localhost:8080"
            , "User-Agent: curl/7.54.0"
            , "Accept: */*"
            , ""
        ])

        self.simpleStrPostRequest = "\r\n".join([
              "POST /hello HTTP/1.1"
            , "Host: localhost:8080"
            , "User-Agent: curl/7.54.0"
            , "Accept: */*"
            , "Content-Type: application/json"
            , "Content-Length: 9"
            , ""
            , "{\"a\":123}"
        ])

        self.getRequest = Request.fromString(self.simpleStrGetRequest)
        self.postRequest = Request.fromString(self.simpleStrPostRequest)

    def test_methodParsing(self):
        self.assertEqual(self.getRequest.method, "GET")
        self.assertEqual(self.postRequest.method, "POST")

    def test_pathParsing(self):
        self.assertEqual(self.getRequest.path, "/hello/ginger")
        self.assertEqual(self.postRequest.path, "/hello")

    def test_queryParamParsing(self):
        self.assertEqual(self.getRequest.queryParams, {"a": "123"})
        self.assertEqual(self.postRequest.queryParams, {})

    def test_headersParsing(self):
        headers = self.postRequest.headers
        self.assertEqual(headers["Host"], "localhost:8080")
        self.assertEqual(headers["User-Agent"], "curl/7.54.0")
        self.assertEqual(int(headers["Content-Length"]), 9)
        self.assertEqual(len(headers), 5)

    def test_bodyParsing(self):
        self.assertEqual(self.getRequest.body, "")
        self.assertEqual(self.postRequest.body, "{\"a\":123}")

if __name__ == '__main__' :
    unittest.main()
