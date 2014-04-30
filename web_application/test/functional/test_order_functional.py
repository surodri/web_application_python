import unittest
from webtest import TestApp

class FunctionalTestOrder(unittest.TestCase):
    def test_order_functional(self):
        app = TestApp('http://localhost:8888')
        resp = app.get('/order/1')
        assert resp.status_int == 200
        assert '{"order_id": 1}' in resp.body
