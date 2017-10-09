#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from json_environ import Environ
from json_environ.json_environ import DEFAULT_ENV_PATH


class TestJsonEnviron(unittest.TestCase):

    def setUp(self):
        self.env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_env.json")

    def test_default_env_path(self):
        if os.path.exists(DEFAULT_ENV_PATH):
            with open(DEFAULT_ENV_PATH, 'r') as default_env_file:
                env = Environ()
                self.assertEqual(str(env), default_env_file.read())
        else:
            with self.assertRaises(FileNotFoundError):
                env = Environ()

    def test_custom_env_path(self):
        env = Environ(path=self.env_path)
        with open(self.env_path, 'r') as custom_env_file:
            self.assertEqual(str(env), custom_env_file.read())

    def test_existing_key(self):
        env = Environ(path=self.env_path)
        self.assertEqual(env("SECRET"), "secret")
        self.assertEqual(env("SECRET", default=True), "secret")
        self.assertEqual(env("NUMBER"), 3)
        self.assertEqual(env("NUMBER", default=True), 3)
        self.assertEqual(env("DEBUG"), True)
        self.assertEqual(env("WRONG"), False)
        self.assertEqual(env("NULL"), None)
        self.assertEqual(env("LIST"), ["*"])
        self.assertEqual(env("NESTED"), {"NAME": "test", "PASSWORD": 123, "LIST": ["*"], "another": {"ONE": 1.0}})

    def test_not_existing_key_with_default(self):
        env = Environ(path=self.env_path)
        self.assertEqual(env("NOTHING", default=True), True)

    def test_not_existing_key(self):
        env = Environ(path=self.env_path)
        with self.assertRaises(KeyError):
            env("nope")

    def test_existing_nested_key(self):
        env = Environ(path=self.env_path)
        self.assertEqual(env("NESTED:NAME"), "test")
        self.assertEqual(env("NESTED:NAME", default=True), "test")
        self.assertEqual(env("NESTED:PASSWORD"), 123)
        self.assertEqual(env("NESTED:PASSWORD", default=True), 123)
        self.assertEqual(env("NESTED:LIST"), ["*"])
        self.assertEqual(env("NESTED:another:ONE"), 1.0)
        self.assertEqual(env("NESTED:another"), {"ONE": 1.0})

    def test_not_existing_nested_key(self):
        env = Environ(path=self.env_path)
        with self.assertRaises(KeyError):
            env("NESTED:nope")
        with self.assertRaises(KeyError):
            env("nope:nope")

    def test_not_existing_nested_key_with_default(self):
        env = Environ(path=self.env_path)
        self.assertEqual(env("NESTED:nope", default='ok'), 'ok')
        self.assertEqual(env("nope:nope:nope", default='ok'), 'ok')

    def test_custom_separator(self):
        env = Environ(path=self.env_path, key_separator=">")
        with self.assertRaises(KeyError):
            env("NESTED>nope")
        with self.assertRaises(KeyError):
            env("NESTED:NAME")

        self.assertEqual(env("NESTED>nope", default='ok'), 'ok')
        self.assertEqual(env("NESTED>NAME", default=True), "test")
        self.assertEqual(env("NESTED>NAME"), "test")
