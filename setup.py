#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-fluent-comments',
    version='0.1.0',
    license='Apache License, Version 2.0',

    install_requires=[
        'Django>=1.2.0',
        'django-crispy-forms>=1.1.1',
    ],
    description='A modern, ajax-based appearance for django.contrib.comments',
    long_description=open('README.rst').read(),

    author='Diederik van der Boor',
    author_email='opensource@edoburu.nl',

    url='https://github.com/edoburu/django-fluent-comments',
    download_url='https://github.com/edoburu/django-fluent-comments/zipball/master',

    packages=find_packages(),
    include_package_data=True,

    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
