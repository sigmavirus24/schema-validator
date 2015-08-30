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
import argparse

from . import docerator
from . import metadata
from . import validation


def _make_argument_parser(prog, register_func):
    parser = argparse.ArgumentParser(prog=prog)
    parser.add_argument(
        '-V', '--version', action='version',
        version='%(prog)s version {0}'.format(metadata.__version__),
    )
    parser.add_argument(
        '-q', '--quiet', action='store_true',
        help='Silence any output from the tool'
    )
    parser.add_argument(
        'schema',
        help='Path to the JSON schema file used for validation',
    )
    register_func(parser)
    return parser


def register_validator_args(parser):
    parser.add_argument(
        'yaml',
        help='Path to the YAML file to validate',
    )


def register_docerator_args(parser):
    parser.add_argument(
        'output',
        help='Path to the file to output to',
    )


def validator_main():
    """Entry-point and controlling function for schema-validator."""
    parser = _make_argument_parser('schema-validator',
                                   register_validator_args)
    args = parser.parse_args()
    result = validation.validate(schema=args.schema, yaml=args.yaml)
    if result and args.quiet:
        result = 1
    parser.exit(result)


def docerator_main():
    """Entry-point for the schema-docerator."""
    parser = _make_argument_parser('schema-docerator',
                                   register_docerator_args)
    args = parser.parse_args()
    result = docerator.docerate(schema=args.schema, outputfile=args.output)
    if result and args.quiet:
        result = 1
    parser.exit(result)


if __name__ == '__main__':
    validator_main()
