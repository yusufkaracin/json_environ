=====
Usage
=====

1. Define env file
___________________

To define env file, simply create JSON file.

2. Using env file
__________________

When you create an instance from `json_environ.Environ`, it will try to read `~/.env.json` as default. You can pass
custom path of your env file to `path` parameter::

    from json_environ import Environ

    env = Environ()  # read ~/.env.json
    # or
    env = Environ(path='some-path/.env.json')
    some_env_value = env("SOME_KEY", default=False)  # get value of SOME_KEY from file. if it isn't exist, return False
    another_value = env("NOT_EXIST")  # raise KeyError if key is not found

3. Reaching nested fields
_________________________

If you have nested structure in your JSON file, you can reach them by using `:` as default::

    env("PARENT:CHILD", default=None)

If you want to custom separator, you can use `key_separator`::

    env = Environ(key_separator=">")
    env("PARENT>CHILD", default=None)

Example
________

Let's assume we have JSON file named `.my_env.json` which looks like::

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

