# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='csv2xml4odoo',
    version='1.0',
    url='https://github.com/MahametH/csv2xml4odoo',
    license='AGPL',
    author='Mahamet Habibou',
    author_email='habibou776@gmail.com',
    description='Convert csv to odoo xml data in Odoo ERP context',
    install_requires=['click'],
    packages=find_packages(),
    long_description=open('README.md').read(),
    zip_safe=False,
    entry_points=dict(
        console_scripts=['oc2x=csv2xml4odoo.csv2xml:main'])
)
