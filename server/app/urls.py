from app.views.views_index import IndexHandler as IndexHandler
from app.views.robot_index import RobotHandler as RobotHandler

# 配置路由视图映射规则
urls = [
    (r"/", RobotHandler),
    (r"/index", IndexHandler),
]
