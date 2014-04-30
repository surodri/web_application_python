from tornado.web import RequestHandler
from models.order import Order

class OrderHandler(RequestHandler):
    def get(self, id):
        self.write(Order.get(id))
