schema-validator (for lack of a better name)
============================================

A tiny tool to accept a JSON schema and apply it to an YAML file that should 
be following the schema. When editing some YAML files, some people find it 
confusing and have trouble writing the YAML they need to. Provided there's a 
schema for the file in question, this tool will analyze your YAML file and 
alert you to any schema violations.

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
