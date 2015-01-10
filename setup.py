# Copyright 2015 Ian Cordasco
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import setuptools
from schema_validator import metadata


def get_long_description():
    desc = ''
    with open('README.rst', 'r') as fd:
        desc = fd.read()
    return desc


setuptools.setup(
    name=metadata.__name__,
    version=metadata.__version__,
    description=metadata.__description__,
    long_description=get_long_description(),
    author=metadata.__author__,
    author_email=metadata.__author_email__,
    license=metadata.__license__,
    classifiers=metadata.__classifiers__,
    packages=setuptools.find_packages(exclude=['examples/*']),
    install_requires=['jsonschema', 'rfc3986', 'pyyaml'],
    entry_points={
        'console_scripts': [
            'schema-validator = schema_validator.main:main',
        ]
    },
)
