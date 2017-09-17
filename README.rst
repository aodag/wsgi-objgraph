=============================
wsgi-objgraph
=============================

.. image:: https://travis-ci.org/aodag/wsgi-objgraph.svg?branch=master
    :target: https://travis-ci.org/aodag/wsgi-objgraph

``wsgi-objgraph`` is wsgi middleware for `objgraph <https://mg.pov.lt/objgraph/>`_.

wsgi middleware
--------------------------


``wsgi-objgraph`` provides middleware::

  app = wsgiobjgraph(app)

You can see counts of most common types at ``.objgraph/most_common_types``.

paste filter
----------------------------------

``wsgi-objgraph`` has entry point to ``paste.filter_factory``.

::

   [pipeline:main]
   pipeline =
     egg:wsgi-objgraph
     yourapp
 
