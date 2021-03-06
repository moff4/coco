#!/usr/bin/env python3
import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='coco',
    version='0.9.5',
    author='Komissarov Andrey',
    author_email='Komissar.off.andrey@mail.ru',
    description='Password brutter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/moff4/coco',
    install_requires=[],
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
