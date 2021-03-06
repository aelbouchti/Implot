# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.txt') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Implot',
    version='1.0.0',
    description='Implot Driver',
    long_description=readme,
    author='Imperial Creaitivy Laboratories',
    author_email='hilalyamine@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
