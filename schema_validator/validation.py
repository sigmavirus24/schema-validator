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
"""Module containing all of the validation logic for schema-validator."""
import json
import re

import jsonschema
import netaddr
import rfc3986
import yaml


@jsonschema.FormatChecker.cls_checks('uri')
def _validate_uri(instance):
    return rfc3986.is_valid_uri(instance, require_scheme=True,
                                require_authority=True)


@jsonschema.FormatChecker.cls_checks('cidr')
def _validate_cidr_format(cidr):
    try:
        netaddr.IPNetwork(cidr)
    except netaddr.AddrFormatError:
        return False
    if '/' not in cidr:
        return False
    if re.search('\s', cidr):
        return False
    return True


def validate(**kwargs):
    """Accept the yaml file and the schema file with which we will validate."""
    yaml_file = kwargs.pop('yaml')
    schema_file = kwargs.pop('schema')

    with open(yaml_file) as fd:
        parsed_yaml = yaml.load(fd)

    with open(schema_file) as fd:
        parsed_schema = json.load(fd)

    validator = jsonschema.validators.Draft4Validator(parsed_schema)

    try:
        validator.validate(parsed_yaml)
    except jsonschema.exceptions.SchemaError as error:
        return str(error)

    return 0
