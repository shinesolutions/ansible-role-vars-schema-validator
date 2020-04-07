#!/usr/bin/python
'''Python library file for Ansible module vars_schema_validator'''
import os
import yaml
from ansible.module_utils.basic import AnsibleModule
from cerberus import Validator

DOCUMENTATION = '''
---
module: vars_schema_validator
short_description: Validate Ansible variables against a YAML schema
description:
    - The module is used to validate variables against a YAML schema.
	  Detailed error messages will be provided when the validation fails.
	  The YAML schema must meet the validation rules defined in cerberus:
	  http://docs.python-cerberus.org/en/stable/validation-rules.html .
version_added: "2.7"
author: "Rongjun XIE (@rJunx)"
options:
    var:
        description:
            - Dictionary variable to be validated against the schema
		type: dict
        required: true
        default: none
        choices:
            - disable
    schema:
        description:
            - Path to YAML schema containing validation rules
		type: str
        required: true
        default: none
        choices:
            - disable
notes:
    - Defining this role at the beginning of a playbook is a good way to ensure
      that only validated variables are used within the playbook
    - Users must provide a correct YAML schema file path in a playbook task
    - Check mode is supported
requirements:
	- python >= 2.7
    - cerberus == 1.3.2
'''

EXAMPLES = '''
name: Validate Ansible variables using the provided YAML schema
vars_schema_validator:
    var: '{{ vars }}'
    schema: schema.yaml
'''

RETURN = '''#'''

def include_constructor(loader, node):
    '''Handler for !include YAML shorthand.'''
    root = os.path.split(loader.stream.name)[0]
    filename = os.path.join(root, loader.construct_scalar(node))
    with open(filename, 'r') as f_stream:
        return yaml.safe_load(f_stream)

yaml.add_constructor('!include', include_constructor, yaml.SafeLoader)

def run_module():
    '''Validate variables against YAML schema.'''
    module_args = dict(
        var=dict(type='dict', required=True),
        schema=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    validator = Validator(allow_unknown=True)
    data = module.params['var']

    with open(module.params['schema'], 'r') as stream:
        try:
            schema = yaml.safe_load(stream)

            if validator.validate(data, schema):
                module.exit_json(
                    changed=False,
                    msg="All variables have been validated successfully."
                )
            else:
                module.fail_json(msg=validator.errors)

        except yaml.YAMLError as err:
            module.fail_json(msg=err)

def main():
    '''Run module to validate variables against YAML schema.'''
    run_module()

if __name__ == '__main__':
    main()
