import tornado.web
from handlers.index import IndexHandler, JsonHandler, HeadersHandler, StatusHandler
import config


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/json", JsonHandler),
            (r"/headers", HeadersHandler),
            (r"/status", StatusHandler),
        ]
        super(Application, self).__init__(handlers, **config.settings)
