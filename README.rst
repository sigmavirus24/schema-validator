schema-validator (for lack of a better name)
============================================

A tiny tool to accept a JSON schema and apply it to an YAML file that should 
be following the schema. When editing some YAML files, some people find it 
confusing and have trouble writing the YAML they need to. Provided there's a 
schema for the file in question, this tool will analyze your YAML file and 
alert you to any schema violations.

Install
-------

.. code-block:: bash

    $ pip install -e git+git://github.com/sigmavirus24/schema-validator

Usage
-----

.. code-block:: bash

    $ schema-validator examples/os-ansible-deployment/user_variables{_schema.json,.yml}
    # or
    $ python -m schema_validator examples/os-ansible-deployment/user_variables{_schema.json,.yml}
    $ echo $?
    0
    $ schema-validator examples/os-ansible-deployment/rpc_user_config{_schema.json,.yml}

Development
-----------

1. Make a virtual environment, e.g.,

   .. code-block:: bash

       $ virtualenv .venv/
       $ . .venv/bin/activate

2. Install the requirements, e.g.,

   .. code-block:: bash

       $ pip install -r requirements.txt

3. Develop!

License
-------

Apache 2.0
