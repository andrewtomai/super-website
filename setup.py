"""
AndrewTomai python package configuration.

Andrew Tomai <atomai@umich.edu>
"""

from setuptools import setup

setup(
    name='andrewtomai',
    version='0.1.0',
    packages=['andrewtomai'],
    include_package_data=True,
    install_requires=[
        'Flask==0.12.2',
        'html5validator==0.2.8',
        'pycodestyle==2.3.1',
        'pydocstyle==2.0.0',
        'pylint==1.7.4',
        'nodeenv==1.2.0',
        'sh==1.12.14',
        'Flask-Testing==0.6.2',
        'selenium==3.6.0',
        'requests==2.18.4',
        'arrow==0.10.0'
    ],
)
