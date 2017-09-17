from setuptools import setup, find_packages


setup(
    name="wsgi-objgraph",
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    author="Atsushi Odagiri",
    author_email="aodagx@gmail.com",
    packages=find_packages(exclude=["example", "tests"]),
    install_requires=[
        "objgraph",
    ],
    extras_require={
        "testing": [
            "pytest",
            "webtest",
        ],
        "dev": [
            "webob",
            "waitress",
            "pastescript",
        ],
    },
)
