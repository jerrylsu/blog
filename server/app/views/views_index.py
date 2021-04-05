import tornado.web

# 定义首页视图
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        return self.write("<h1>Hello Jerry!</h1>")