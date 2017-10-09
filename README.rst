============
JSON Environ
============


.. image:: https://img.shields.io/pypi/v/json_environ.svg
        :target: https://pypi.python.org/pypi/json_environ

.. image:: https://readthedocs.org/projects/json-environ/badge/?version=latest
        :target: https://json-environ.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status



Utilize environment variables from JSON file to configure your Python application. Inspired from `django-environ`_.

.. _django-environ: https://github.com/joke2k/django-environ


* Free software: MIT license
* Documentation: https://json-environ.readthedocs.io.

=====
Quick Example
=====

Let's assume we have JSON file like::

    {
      "SECRET_KEY": "kminvupn=7dbw70e!#njo8qas2bx$tmw$nv1pt$g30&+f4(8c)",
      "DEBUG": true,
      "SSL": false,
      "ALLOWED_HOSTS": [
        "*"
      ],
      "DATABASE": {
        "NAME": "dbname",
        "USER": "dbuser",
        "PASSWORD": "dbsecret"
      }
    }

To use `JSON Environ` in a project::

    import os

    from json_environ import Environ

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(BASE_DIR, '.my_env.json')
    env = Environ(path=env_path)

    SECRET_KEY = env('SECRET_KEY', default="PT09PT0KVXNhZ2UKPT09PT0KClRvI")
    DEBUG = env("DEBUG")
    ALLOWED_HOSTS = env('ALLOWED_HOSTS')
    if env('SSL', default=False) is True:
        SECURE_SSL_REDIRECT = False

    DATABASES = {
        'default': {
            'NAME': env("DATABASE:NAME", default="test"),
            'USER': env("DATABASE:USER", default="lms"),
            'PASSWORD': env("DATABASE:PASSWORD", default="123456"),
        }
    }

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

