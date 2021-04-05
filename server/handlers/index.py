import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<html><head>Hello, Jerry!</head></html>")


class JsonHandler(tornado.web.RequestHandler):
    def get(self):
        json_ = {
            "name": "Jerry",
            "id": 1,
        }
        self.set_header("jerry", "yeah")
        self.write(json_)


class HeadersHandler(tornado.web.RequestHandler):
    def set_default_headers(self) -> None:
        self.set_header("Annie", "ok")

    def get(self):
        self.write("jerry")


class StatusHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_status(404)
        self.write("*" * 20)
