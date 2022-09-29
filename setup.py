from setuptools import setup

version = '0.1.2'

long_description = '''
It provides a simple interface for quick and convenient work with MariaDB.
'''

setup(
    name='sqlib',

    version=version,

    packages=['sqlib'],
    install_requires=['mariadb'],

    url='https://github.com/meyiapir/sqlib',

    license='Apache License, Version 2.0, see LICENSE file',

    author='meyap',

    author_email='mmeyiapir@gmail.com',

    description='Sqlib is a small ORM for MariaDB.',

    long_description=open('README.md').read(),
)
