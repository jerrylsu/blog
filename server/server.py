import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from application import Application
import config

from tornado.options import define, options
define("port", default=8180, help="run port", type=int)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
