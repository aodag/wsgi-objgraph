import pytest
import webtest


def dummy_app(environ, start_response):
    start_response("200 OK",
                   [('Content-Type', 'text/plain')])
    return [b"Hello"]


class TestFilter(object):

    @pytest.fixture
    def target(self):
        from wsgiobjgraph.paste import filter_factory
        return filter_factory

    def test_no_filter(self, target):
        filter = target({})
        filtered_app = filter(dummy_app)
        app = webtest.TestApp(filtered_app)
        result = app.get('/')
        assert result.text == "Hello"

    def test_filtered_path(self, target):
        filter = target({})
        filtered_app = filter(dummy_app)
        app = webtest.TestApp(filtered_app)
        result = app.get('/.objgraph/most_common_types')
        assert "ObjGraph most common types" in result
