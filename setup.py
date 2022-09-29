from setuptools import setup

version = '0.1.8'

long_description = '''
It provides a simple interface for quick and convenient work with MariaDB.
'''

setup(
    name='sqlib',

    version=version,

    packages=['sqlib', 'sqlib.modules'],
    install_requires=['mariadb'],

    url='https://github.com/meyiapir/sqlib',

    license='Apache License, Version 2.0, see LICENSE file',

    author='meyap',

    author_email='mmeyiapir@gmail.com',

    description='Sqlib is a small ORM for MariaDB.',

    description_content_type='text/markdown',

    long_description=long_description,
    long_description_content_type='text/markdown',
)
