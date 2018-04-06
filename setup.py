# Copyright (c) 2018 Ilya Shchepetkov
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

import setuptools

setuptools.setup(
    name='eventb-to-txt',
    version='1.0',
    author='Ilya Shchepetkov',
    author_email='ilya.shchepetkov@yandex.ru',
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    packages=['eventb_to_txt'],
    entry_points={
        'console_scripts': [
            'eventb-to-txt=eventb_to_txt.__main__:main',
        ],
    }
)
