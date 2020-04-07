[![Build Status](https://github.com/shinesolutions/ansible-role-vars-schema-validator/workflows/CI/badge.svg)](https://github.com/shinesolutions/ansible-role-vars-schema-validator/actions?query=workflow%3ACI)
[![Known Vulnerabilities](https://snyk.io/test/github/shinesolutions/ansible-role-vars-schema-validator/badge.svg)](https://snyk.io/test/github/shinesolutions/ansible-role-vars-schema-validator)

Ansible Role Vars Schema Validator
----------------------------------

Ansible Role for validating Ansible variables against a YAML schema.

## PREREQUISITES

- Requires Ansible 2.4 or newer
- Requires cerberus 1.3.2
    - [Install Guide](https://docs.python-cerberus.org/en/stable/install.html)

## PLAYBOOK
There is one demo playbook includes. All varibles and schemas are located in `exmaple` folder.

  - example/test_var.yaml:
    It contains all variables used in the playbook.

  - example/schema.yaml:
    It is the root schema for the variables, which is able to include child schemas with `!include`.

  - example/schema_1.yaml:
    It is the child schema for the variables, which is loaded in the root schema.

Run with `ansible-playbook test.yml` to see the results.

## Usage
Add
```
  roles:
    - role: 'validator'
      vars:
        schema: 'path/to/your/schema'
```
to your ansible playbook to use variable validator.
More details are referred to [Ansible Role](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html).
