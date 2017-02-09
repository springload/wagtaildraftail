#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='wagtail-draftail',
    version='0.1a',
    description='Draft.js editor for Wagtail, built upon Draftail and draftjs_exporter',
    author='Springload',
    author_email='hello@springload.co.nz',
    url='https://github.com/springload/wagtaildraftail',
    packages=find_packages(),
    install_requires=[
        'draftjs-exporter==0.6.2',
    ]
)
