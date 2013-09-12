# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '0.1'

setup(
    name='bobtemplates.plonegovbr',
    version=version,
    description="Templates para projetos PloneGov.Br.",
    long_description=open("README.rst").read(),
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
    ],
    keywords='',
    author='PloneGov.Br',
    author_email='gov@plone.org.br',
    url='https://github.com/plonegovbr/bobtemplates.plonegovbr',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['bobtemplates'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'mr.bob',
    ],
    extras_require={
        'test': [
            'nose',
            'nose-selecttests',
            'scripttest',
            'unittest2',
        ]
    },
    entry_points={},
)
