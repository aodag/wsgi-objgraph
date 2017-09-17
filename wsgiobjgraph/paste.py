from . import Middleware


def filter_factory(global_conf, **app_conf):
    def filter(app):
        return Middleware(app)
    return filter
