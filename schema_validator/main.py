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

from . import metadata
from . import validation


def _make_argument_parser():
    parser = argparse.ArgumentParser(prog='yaml-schema-validator')
    parser.add_argument(
        '-V', '--version', action='version',
        version='%(prog)s version {0}'.format(metadata.__version__),
    )
    parser.add_argument(
        'schema',
        help='Path to the JSON schema file used for validation',
    )
    parser.add_argument(
        'yaml',
        help='Path to the YAML file to validate',
    )
    return parser


def main():
    """Entry-point and controlling function for schema-validator."""
    parser = _make_argument_parser()
    args = parser.parse_args()
    parser.exit(validation.validate(schema=args.schema, yaml=args.yaml))


if __name__ == '__main__':
    main()
