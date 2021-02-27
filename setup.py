# ==============================================================================
# Name: setup.py
# Author: Bloom, Matthew 
# Date: 02/24/2020
# Revision: 1.0.0
#
# ==============================================================================
# Description
# ------------------------------------------------------------------------------
# Setup
#
# ==============================================================================
# History
# ------------------------------------------------------------------------------
# Revision on https://github.com/mbloom88/inv-mgr
# 
# ==============================================================================

# ==============================================================================
# IMPORTS
# ==============================================================================

from setuptools import setup, find_packages

# ==============================================================================
# SETUP
# ==============================================================================

setup(
    name="inv-mgr",
    version="1.0.0",
    author="Matthew Bloom",
    author_email="matthewabloom88@gmail.com",
    description="Inventory Manager GUI for a mechanical fastener database.",
    url="https://github.com/mbloom88/inv-mgr",
    packages=find_packages(include=['inv-mgr', 'inv-mgr.*']),
    install_requires=[
        'PyQt5==5.15.2', ### primary_1
        'PyQt5-Qt==5.15.2',
        'PyQt5-sip==12.8.1',
        'pyqt5-tools==5.15.2.3.0.2', ### primary_2
        'click==7.1.2',
        'pyqt5-plugins==5.15.2.2.0.1',
        'python-dotenv==0.15.0',
        'qt5-applications==5.15.2.2.1',
        'qt5-tools==5.15.2.1.0.1',
        'PyOpenGL==3.1.5', ### primary_3
        'pyinstaller==4.2' ### primary_4
        'altgraph==0.17',
        'future==0.18.2',
        'pefile==2019.4.18',
        'pyinstaller-hooks-contrib==2020.11',
        'pywin32-ctypes==0.2.0',
        'auto-py-to-exe==2.8.0', ### primary_5
        'bottle==0.12.19', 
        'bottle-websocket=0.2.9',
        'cffi=1.14.5'
        'Eel==0.12.4',
        'gevent=21.1.2',
        'gevent-websocket==0.10.1',
        'greenlet==1.0.0',
        'pycparser==2.20',
        'whichcraft==0.6.1',
        'zope.event==4.5.0',
        'zope.interface==5.2.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)
