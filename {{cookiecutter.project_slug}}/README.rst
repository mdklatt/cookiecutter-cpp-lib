{% set delim = "=" * cookiecutter.lib_name|length -%}
{{ delim }}
{{ cookiecutter.lib_name }}
{{ delim }}

C++ library project created from the `mdklatt/cookiecutter-cpp-lib`_ template.


===========
Development
===========

Create the development environment:

.. code-block::

    $ make dev


Build the project:

.. code-block::

    $ make build


Run tests:

.. code-block::

    $ make test


Build documentation:

.. code-block::

    $ make docs


.. _mdklatt/cookiecutter-cpp-lib: https://github.com/mdklatt/cookiecutter-cpp-lib
