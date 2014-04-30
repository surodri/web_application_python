import re
import struct
class Parser():
    def parse_message(self, message_log):
        message_bytes = re.split('\s+', message_log)
        message_type = self.hex_to_int(message_bytes[1])
        message_parsed= {}
        message_parsed['message_type'] = message_type
        return message_parsed

    def hex_to_int(self, value):
        return int (value, 16)
