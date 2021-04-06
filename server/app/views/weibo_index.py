import tornado.web
import tornado.httpclient
import urllib
import json


class WeiboHandler(tornado.web.RequestHandler):
    """构建一个向微博搜索API发送HTTP请求的简单Web应用。
    这个Web应用有一个参数q作为查询字符串，并确定多久会出现
    一条符合搜索条件的推文被发布在微博上（"每秒推数"）
    """
    def get(self):
        query = self.get_argument("q")
        client = tornado.httpclient.HTTPClient()
        response = client.fetch("http://api.t.sina.com.cn/search.json?" + \
                                urllib.urlencode({"q": query, "rpp": 100}))
        body = json.loads(response.body)
        result_cnt = len(body["results"])
        self.write(result_cnt)
        pass
