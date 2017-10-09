# -*- coding: utf-8 -*-
import os
import json

DEFAULT_ENV_PATH = "{home}/.env.json".format(home=os.path.expanduser("~"))
DEFAULT_KEY_SEPARATOR = ":"


class NoValue(object):
    pass


class Environ(object):
    __NOTSET = NoValue()

    def __init__(self, path=None, key_separator=DEFAULT_KEY_SEPARATOR):
        self.__path = path if path else DEFAULT_ENV_PATH
        self.key_separator = key_separator

        if not os.path.exists(self.__path):
            raise FileNotFoundError('Is "{}" exist?'.format(self.__path))
        with open(self.__path, 'r') as env_file:
            self.__as_str = env_file.read()
            self._env = json.loads(self.__as_str)

    def __call__(self, key, default=__NOTSET):
        first_key, keys = self._separate_key(key=key)
        try:
            structure = self._env[first_key]
            for nested_key in keys:
                structure = structure[nested_key]
            return structure
        except KeyError:
            if default is self.__NOTSET:
                raise KeyError("{key} is not found in {path}"
                               .format(key=key, path=self.__path))
            return default

    def __str__(self):
        return self.__as_str

    def _separate_key(self, key):
        keys = key.split(sep=self.key_separator)
        first_key = keys.pop(0)
        return first_key, keys
