[![Build Status](https://github.com/shinesolutions/ansible-role-vars-schema-validator/workflows/CI/badge.svg)](https://github.com/shinesolutions/ansible-role-vars-schema-validator/actions?query=workflow%3ACI)
[![Known Vulnerabilities](https://snyk.io/test/github/shinesolutions/ansible-role-vars-schema-validator/badge.svg)](https://snyk.io/test/github/shinesolutions/ansible-role-vars-schema-validator)

Ansible Role Vars Schema Validator
----------------------------------

Ansible Role for validating Ansible variables against a YAML schema.

This role is useful for making sure that the Ansible variables required for your playbooks are valid according to the specified schema, where you can define whether a variable must be a string, or if the variable is mandatory, and various other use cases supported by [Cerberus](https://docs.python-cerberus.org/en/stable/validation-rules.html).

| Ansible Version | Ansible Role Vars Schema Validator Version |
|-----------------|--------------------------------------------|
| 4.x             | 1.1.0                                      |
| 3.x             | 1.0.0                                      |
| 2.x             | 0.10.0                                     |

Installation
------------

Install [Cerberus](https://pypi.org/project/Cerberus/) Python package:

    pip install cerberus==1.3.2

Add vars_schema_validator role to `requirements.yml` file:

    - src: shinesolutions_opensource.vars_schema_validator
      path: roles/

Install Ansible roles using `ansible-galaxy`:

    ansible-galaxy install --role-file requirements.yml --force

Usage
-----

Create a validation schema file using [the rules defined in cerberus](http://docs.python-cerberus.org/en/stable/validation-rules.html).

Add the role to playbook and specify the schema path:

    roles:
      - role: 'shinesolutions_opensource.vars_schema_validator'
        vars:
          schema: 'path/to/your/schema.yaml'

In the `path/to/your/schema.yaml` file, specify the validation rules.

Required and can't be empty:

    some_var:
      required: true
      empty: false

Should be a string and from a predefined list:

    some_var:
      type: string
      allowed:
        - some_value_1
        - some_value_2

Should be an integer:

    some_var:
      type: integer

Should be a boolean:

    some_var:
      type: boolean

Should be a list:

    some_var:
      type: list

Should be a dictionary/map:

    some_var:
      type: dict

Only allow configuration properties which are defined in the schema:
Note that this setting is applied to all descendant properties.

    some_var:
      allow_unknown: false
