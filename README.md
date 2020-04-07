[![Build Status](https://github.com/shinesolutions/ansible-role-vars-schema-validator/workflows/CI/badge.svg)](https://github.com/shinesolutions/ansible-role-vars-schema-validator/actions?query=workflow%3ACI)
[![Known Vulnerabilities](https://snyk.io/test/github/shinesolutions/ansible-role-vars-schema-validator/badge.svg)](https://snyk.io/test/github/shinesolutions/ansible-role-vars-schema-validator)

Ansible Role Vars Schema Validator
----------------------------------

Ansible Role for validating Ansible variables against a YAML schema.

Installation
------------

Add vars_schema_validator role to `requirements.yml` file:

    - src: shinesolutions_opensource.vars_schema_validator
      path: roles/

Download Ansible roles using `ansible-galaxy`:

    ansible-galaxy install -r requirements.yml --force

Usage
-----

Create a validation schema file using [the rules defined in cerberus](http://docs.python-cerberus.org/en/stable/validation-rules.html).

Add the role to playbook and specify the schema path:

    roles:
      - role: 'validator'
        vars:
          schema: 'path/to/your/schema.yaml'
