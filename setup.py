"""A setup file for the joystick uart package

"""
from setuptools import setup
from setuptools import find_packages

# To use consistent encoding
from codecs import open
from os import path

setup(
    name='joystick_uart',

    version='1.0.0',

    description='Application to send joystick commands over UART',

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
    ],

    entry_points = {
        "console_scripts": [
            "joystick_uart = joystick_uart.joystick_uart:main"
        ]
    }
)
