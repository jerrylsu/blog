import os
BASE_DIR = os.path.dirname(__file__)

options = {
    "port": 8180
}

settings = {
    "static_path": os.path.join(BASE_DIR, "static"),
    "template_path": os.path.join(BASE_DIR, "templates"),
    "debug": True,
}
