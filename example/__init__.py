import logging
from webob.dec import wsgify
import wsgiobjgraph


logging.basicConfig(level=logging.DEBUG)


class Dummy(object):
    pass


dummies = []


@wsgify
def application(request):
    dummies.append(Dummy())
    return "hello"


application = wsgiobjgraph.Middleware(application)
