import unittest
from audit_trail_system.models.parsers.tms23.messages.new_order import NewOrder
class TestNewOrder(unittest.TestCase):
    client_order_id = '01 00 00 00 '

    new_order_message = (client_order_id + '\n')
    def test_should_parse_client_order_id(self):
        message = NewOrder().parse(self.new_order_message)
        self.assertEqual(message['client_order_id'],1)
