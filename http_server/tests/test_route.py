import unittest
import re
from ..route import Route


class TestRoute(unittest.TestCase):

    def setUp(self):
        self.prefix = "/api/v1/"
        self.exp = "/user/:name/post/:id"
        self.path = "/api/v1/user/ginger/post/123"
        self.route = Route("GET", self.prefix, self.exp, (lambda x: x))

    def test_regexGenerating(self):
        res = self.route.regex.match(self.path)
        varDict = res.groupdict()
        self.assertEqual(varDict["name"], "ginger")
        self.assertEqual(varDict["id"], "123")
