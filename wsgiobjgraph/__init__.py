import logging
import objgraph
from cgi import parse_qs


logger = logging.getLogger(__name__)


def most_common_types_app(environ, start_response):
    limit = 1000
    if environ.get("QUERY_STRING"):
        query = parse_qs(environ.get("QUERY_STRING", ""))
        if "limit" in query:
            limit = int(query["limit"][0])
    types = objgraph.most_common_types(limit=limit)
    html = [
        "<html>",
        "<head>",
        "<title>ObjGraph most common types</title>"
        "</head>",
        "<body>",
        "<table>",
        "<tr><th>type</th><th>count</th></tr>",
    ]
    logger.debug("common_types: %s", types)
    for typename, count in types:
        parts = [
            "<tr>",
            "<td>",
            typename,
            "</td>",
            "<td>",
            str(count),
            "</td>",
            "</tr>",
        ]
        html += parts
    html += [
        "</table>",
        "</body>",
        "</html>",
    ]
    start_response(
        "200 OK",
        [('Content-type', 'text/html')],
    )
    html = [h.encode('utf-8') for h in html]
    return html


class Middleware(object):
    apps = {
        '.objgraph/most_common_types': most_common_types_app,
    }

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '').strip('/')
        if path in self.apps:
            return self.apps[path](environ, start_response)
        return self.app(environ, start_response)
