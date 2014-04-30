import unittest
from audit_trail_system.models.order import Order

class TestOrder(unittest.TestCase):

    def test_order_should_return_1(self):
        json = Order.get(1)
        self.assertEqual('{"order_id": 1}',json)
