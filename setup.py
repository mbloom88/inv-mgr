#!/usr/bin/env python
################################################################################
# \file
# \author Matthew Bloom <matthewabloom88@gmail.com>
# \brief
#
################################################################################

from setuptools import setup, find_packages

################################################################################

setup(
    name="inv-mgr",
    version="1.0.0",
    author="Matthew Bloom",
    author_email="matthewabloom88@gmail.com",
    description="",
    url="https://github.com/mbloom88/inv-mgr",
    packages=find_packages(include=['database', 'database.*']),
    install_requires=[
        'click==7.1.2',
        'PyQt5==5.15.2',
        'pyqt5-plugins==5.15.2.2.0.1',
        'PyQt5-Qt==5.15.2',
        'PyQt5-sip==12.8.1',
        'pyqt5-tools==5.15.2.3.0.2',
        'python-dotenv==0.15.0',
        'qt5-applications==5.15.2.2.1',
        'qt5-tools==5.15.2.1.0.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)
