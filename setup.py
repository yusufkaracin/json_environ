#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []
setup_requirements = []
test_requirements = []

setup(
    name='json_environ',
    version='0.1.0',
    description="Utilize environment variables from JSON file to configure your Python application.",
    long_description=readme + '\n\n' + history,
    author="Yusuf Karaçin",
    author_email='ysfbkrcn@gmail.com',
    url='https://github.com/yusufkaracin/json_environ',
    packages=find_packages(include=['json_environ']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='json environment variables configuration',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
