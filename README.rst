##################
flake8-codeclimate
##################

A Flake8 plugin to generate error reports in a format consumable by Code Climate.

The `full error report specification <https://github.com/codeclimate/spec/blob/master/SPEC.md#data-types>`_
includes a description of Code Climate specific error categories and fields.

Installation
============

Install from PyPI:

.. code-block:: bash

    $ pip install flake8-codeclimate

Or from Git:

.. code-block:: bash

    $ pip install -e git+git://github.com/bennylope/flake8-codeclimate.git#egg=flake8_codeclimate

Usage
=====

Run Flake8 with the format option `codeclimate`::

    flake8 --format=codeclimate


