import tornado.ioloop
import tornado.web
from handlers.order_handler import OrderHandler

application = tornado.web.Application([(r'/order/(\d)',
    OrderHandler),
    ])
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
