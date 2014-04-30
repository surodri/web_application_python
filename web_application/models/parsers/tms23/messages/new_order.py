from struct import Struct
from audit_trail_system.utils.tuples import to_dict
class NewOrder():

    new_order_struct = Struct('I')
    FIELDS = ['client_order_id']
    NEW_ORDER_LENGTH = new_order_struct.size
    def parse(self, message_in_hex):
        message_tuple = self.new_order_struct.unpack(message_in_hex[:self.NEW_ORDER_LENGTH])
        new_order = to_dict(message_tuple, self.FIELDS)
        #new_order['limit_price'] = normalize_price(new_order['limit_price'])
        return new_order
