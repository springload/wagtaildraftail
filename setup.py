#!/usr/bin/env python

from __future__ import absolute_import, unicode_literals

from codecs import open

from wagtaildraftail import __version__

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


install_requires = [
    'draftjs_exporter==0.7.0',
]

# Testing dependencies
testing_extras = [
    # Required for running the tests
    'tox>=2.3.1',

    # For coverage and PEP8 linting
    'coverage>=4.1.0',
    'flake8>=3.2.0',
    'isort>=4.2.5',

    # For test site
    'wagtail==1.9',
]

# Documentation dependencies
documentation_extras = [

]

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='wagtaildraftail',
    version=__version__,
    description='Draft.js editor for Wagtail, built upon Draftail and draftjs_exporter',
    author='Springload',
    author_email='hello@springload.co.nz',
    url='https://github.com/springload/wagtaildraftail',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    long_description=readme,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Editors :: Word Processors',
    ],
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
        'docs': documentation_extras,
    },
    zip_safe=False,
)
