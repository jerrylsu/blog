import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.options import options, define

# define server port
define("port", default=8180, type=int, help="run port")

# define application
class JerryApplication(tornado.web.Application):
    # overwrite __init__
    def __init__(self):
        # 指定路由规则
        handlers = urls
        # 指定配置信息
        settings = configs
        # 调用父类__init__，传入参数
        super(JerryApplication, self).__init__(handlers=handlers, **settings)
        pass

# define service
def create_server():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(
        JerryApplication()
    )
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
