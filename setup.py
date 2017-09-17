from setuptools import setup, find_packages


def _read(fname):
    try:
        with open(fname) as f:
            return f.read()
    except Exception:
        return ""


setup(
    name="wsgi-objgraph",
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    author="Atsushi Odagiri",
    author_email="aodagx@gmail.com",
    packages=find_packages(exclude=["example", "tests"]),
    description="wsgi middleware for objgprah",
    long_description=_read('README.rst'),
    license="MIT",
    url="https://github.com/aodag/wsgi-objgraph",
    install_requires=[
        "objgraph",
    ],
    extras_require={
        "testing": [
            "pytest",
            "pytest-cov",
            "webtest",
        ],
        "dev": [
            "webob",
            "waitress",
            "pastescript",
        ],
    },
    entry_points={
        "paste.filter_factory": [
            "main=wsgiobjgraph.paste:filter_factory",
        ],
    },
)
