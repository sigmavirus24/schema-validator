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
"""Custom URI validator for jsonschema."""
import jsonschema
import rfc3986


def register_uri_format_checker():
    @jsonschema.FormatChecker.cls_checks('uri')
    def validate_uri(instance):
        return rfc3986.is_valid_uri(instance, require_scheme=True,
                                    require_authority=True)
