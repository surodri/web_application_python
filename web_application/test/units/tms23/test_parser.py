import unittest

from audit_trail_system.models.parsers.tms23.parser import Parser
from audit_trail_system.models.parsers.tms23.message_factory import MessageFactory
class TestTMS23Parser(unittest.TestCase):
    NEW_ORDER = 1
    new_order_message = '01 01 44 00 01 00 00 00 47 3F EC 02 00 00 11 00 BB 01 1A 00 32 00 00 00 00 00 00 00 80 4F 12 00 00 00 00 00 00 00 00 00 00 00 00 00 02 03 38 00 5A CB 65 38 02 00 01 00 00 00 00 00 01 00 00 00 F9 8A 21 53'
    modify_order_message = '01 02 5c 00 ' + '01 00 00 00 0D 3A 20 53 ' + (32*"00")

    def test_should_parse_new_order_message_type(self):
        message = Parser().parse_message(self.new_order_message)
        self.assertEqual(message['message_type'], MessageFactory.NEW_ORDER)

    def test_should_parse_modify_order_type(self):
        message = Parser().parse_message(self.modify_order_message)

        self.assertEqual(message['message_type'], MessageFactory.MODIFY_ORDER)
