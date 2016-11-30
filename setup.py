"""A setup file for the joystick uart package

"""
from setuptools import setup
from setuptools import find_packages

# To use consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='joystick_uart',

    version='1.0.0',

    description='Application to send joystick commands over UART',
    long_description=long_description,

    url='https://github.com/nerdgilbert/joystick_uart',

    author='OpenROV',
    author_email='gilbert@openrov.com',

    maintainer='Gilbert Montague',
    maintainer_email='gilbert@openrov.com',

    license='MIT',

    keywords='joystick pygame uart',
    packages=['joystick_uart'],

    install_requires=[
        'argparse',
        'pygame',
        'pyserial'
    ]
)
