import tornado.web
import tornado.httpclient
from urllib import parse
import json


class RobotHandler(tornado.web.RequestHandler):
    async def get(self):
        msg = self.get_argument("msg")
        # tornado 5.0以后只能在服务中使用异步客户端AsyncHTTPClient，非HTTPClient。
        client = tornado.httpclient.AsyncHTTPClient()
        response = await client.fetch("http://api.qingyunke.com/api.php?" + \
                                      parse.urlencode({"msg": msg,
                                                       "key": "free",
                                                       "appid": "0"}))
        body = json.loads(response.body)
        content = body["content"]
        self.write(f"<html>{content}</html>")
        pass
