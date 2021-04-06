import tornado.web
import tornado.httpclient
from urllib import parse
import json


class RobotHandler(tornado.web.RequestHandler):
    """构建一个向微博搜索API发送HTTP请求的简单Web应用。
    这个Web应用有一个参数q作为查询字符串，并确定多久会出现
    一条符合搜索条件的推文被发布在微博上（"每秒推数"）
    """
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
