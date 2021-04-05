from app.views.views_index import IndexHandler as IndexHandler

# 配置路由视图映射规则
urls = [
    (r"/", IndexHandler),
]
