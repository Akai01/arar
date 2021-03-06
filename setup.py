#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["numpy", "pandas", "matplotlib", ]

test_requirements = ['pytest>=3', ]

setup(
    author="Resul Akay",
    author_email='resulakay1@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Time series forecasting using arar algorithm.",
    install_requires=requirements,
    license="MIT license",
    long_description=long_description,
    include_package_data=True,
    keywords='arar',
    name='arar',
    packages=find_packages(include=['arar', 'arar.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/akai01/arar',
    version='0.1.0',
    zip_safe=False,
)
