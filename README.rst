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

.. image:: https://travis-ci.org/GoldenLine/gtlaunch.svg?branch=master
    :target: https://travis-ci.org/GoldenLine/gtlaunch

.. image:: https://coveralls.io/repos/GoldenLine/gtlaunch/badge.png?branch=master
    :target: https://coveralls.io/r/GoldenLine/gtlaunch?branch=master

``gtlaunch`` launches Gnome Terminal with predefined tabs, runs a command
in each tab and leaves you in the shell if the command quits, so you can
jump straight to work. See the demo:

.. image:: http://zippy.gfycat.com/EarlyBlackGrub.gif

Prerequisites
-------------

 * Linux with Gnome
 * ZSH (support for other shells is in the works)
 * Python 2.7 or 3.3+

Installation
------------

The recommended way to install Python packages which provide executable scripts
is to use `pipsi <https://github.com/mitsuhiko/pipsi>`_::

    pipsi install gtlaunch

But ``pip`` also works::

    pip install gtlaunch

Add the following to your ``.zshrc`` (see
`this message <http://www.zsh.org/mla/users/2005/msg00599.html>`_ for an
explanation)::

    if [[ $1 == eval ]]
    then
        "$@"
        set --
    fi

Configuration
-------------

By default, ``gtlaunch`` reads its configuration from a ``gtlaunch.json`` file
located in user's home directory. This can be overridden by passing the
location of config file to ``--config`` option::

    gtlaunch --config ../my-projects.json

Here's an example configuration file (note: JSON does not allow comments,
these are just for reference)::

    {
        // The configuration is an object where keys are project names
        // and values store per-project settings.
        "simple_project": {
            // The simplest setup is just a list of commands under the tabs key
            "tabs": ["vim", "python", "git status"]
        },
        "more_options": {
            // prefix specifies a command that will be run before each tab's
            // command executes
            "prefix": "workon test",
            // you can specify working directory; ~ will be expanded
            "cwd": "~/Development",
            "tabs": [
                // the extended format allows more options, see below
                {
                    // command is required
                    "command": "vim",
                    // title is optional, defaults to command
                    "title": "editor"
                },
                // you can mix&match both formats
                "python",
                "git status"
            ]
        }
    }

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
