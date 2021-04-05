import tornado.web          # web框架
import tornado.httpserver   # http服务
import tornado.ioloop       # 输入输出事件循环
import tornado.options      # 配置工具

from tornado.options import options, define
from app.configs import configs
from app.urls import urls

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
    # 允许命令行启动
    tornado.options.parse_command_line()
    # 创建http服务
    http_server = tornado.httpserver.HTTPServer(
        JerryApplication()
    )
    # 绑定监听端口
    http_server.listen(options.port)
    # 启动事件循环
    tornado.ioloop.IOLoop.instance().start()
