import logging
from webob.dec import wsgify
import wsgiobjgraph


logging.basicConfig(level=logging.DEBUG)


class Dummy(object):
    pass


dummies = []


@wsgify
def app(request):
    dummies.append(Dummy())
    return "hello"


def make_app(global_conf, **app_conf):
    return app


application = wsgiobjgraph.Middleware(app)
