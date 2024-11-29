# The MIT License (MIT)
# 
# Copyright (c) 2014 Andreas Dewes
# Copyright (c) 2018-2020 Abilian SAS
# Copyright (c) 2022 Marcin Kozlowski
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# Blitzdb3 with some changes (see diff)
# Original source/license info and acknowledgements at https://github.com/adewes/blitzdb and https://github.com/abilian/blitzdb3

from setuptools import setup, find_packages

LONG_DESCRIPTION = """\
Blitz is a document-oriented database toolkit for Python that is backend-agnostic.

It comes with a flat-file database for JSON documents and provides MongoDB-like querying capabilities.

Key Features
============

* Document-based, object-oriented interface.
* Powerful and rich querying language.
* Deep document indexes on arbitrary fields.
* Compressed storage of documents.
* Support for multiple backends (e.g. file-based storage, MongoDB).
* Support for database transactions (currently only for the file-based backend).

"""

setup(
    name='blitzdb5',
    version='4.0.19',
    license='MIT',
    url='https://github.com/tcosolutions/blitzdb3',
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    description='A document-oriented database written purely in Python.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown', 
)

