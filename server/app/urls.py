from app.views.views_index import IndexHandler as IndexHandler
from app.views.weibo_index import WeiboHandler as WeiboHandler

# 配置路由视图映射规则
urls = [
    (r"/", WeiboHandler),
    (r"/index", IndexHandler),
]
