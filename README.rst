========
gtlaunch
========

.. image:: https://pypip.in/version/gtlaunch/badge.svg
    :target: https://pypi.python.org/pypi/gtlaunch/
    :alt: Latest PyPI version

.. image:: https://pypip.in/download/gtlaunch/badge.svg
    :target: https://pypi.python.org/pypi/gtlaunch/
    :alt: Number of PyPI downloads

.. image:: https://pypip.in/py_versions/gtlaunch/badge.svg
    :target: https://pypi.python.org/pypi/gtlaunch/
    :alt: Supported Python versions

.. image:: https://pypip.in/wheel/gtlaunch/badge.svg
    :target: https://pypi.python.org/pypi/gtlaunch/
    :alt: Wheel Status

.. image:: https://travis-ci.org/zsiciarz/gtlaunch.svg?branch=master
    :target: https://travis-ci.org/zsiciarz/gtlaunch

.. image:: https://coveralls.io/repos/zsiciarz/gtlaunch/badge.png?branch=master
    :target: https://coveralls.io/r/zsiciarz/gtlaunch?branch=master

Gnome Terminal launcher

Installation
------------

The recommended way to install Python packages which provide executable scripts
is to use `pipsi <https://github.com/mitsuhiko/pipsi>`_::

    pipsi install gtlaunch

But ``pip`` also works::

    pip install gtlaunch

Configuration
-------------

By default, ``gtlaunch`` reads its configuration from a ``gtlaunch.json`` file
located in user's home directory. This can be overridden by passing the
location of config file to ``--config`` option::

    gtlaunch --config ../my-projects.json

TODO: Add example config file with explanations

Resources
---------

 * `Issue tracker <https://github.com/zsiciarz/gtlaunch/issues>`_
 * `CI server <https://travis-ci.org/zsiciarz/gtlaunch>`_

Author
------

 * `Zbigniew Siciarz <http://siciarz.net>`_ (zbigniew at siciarz dot net)

License
-------

gtlaunch is free software, licensed under the MIT/X11 License. A copy of
the license is provided with the source code in the LICENSE file.
