#!/usr/bin/python

# Copyright: (c) 2019, Rongjun XIE <rongjun.xie@shinesolutions.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: vars_schema_validator
short_description: Validate playbook variables with a custom YAML schema.
description:
    - The moduele is used to validate variables with a custom YAML schema.
	  Detailed error messages are provided if the validation fails.
	  The YAML schema must meet the validation rules in cerberus.
	  More details are shown in http://docs.python-cerberus.org/en/stable/validation-rules.html.
version_added: "2.7"
author: "Rongjun XIE (@rJunx)"
options:
    var:
        description:
            - Specify variables required for validation.
		type: dict
        required: true
        default: none
        choices:
            - disable
    schema:
        description:
            - Specify a schema YAML file path for validating the variables.
		type: str
        required: true
        default: none
        choices:
            - disable
notes:
    - To make sure that only validated variables are sent to the cluster and executed,
	  the validation task should be executed at the beginning in the playbook.
    - Users have to provide a correct YAML schema file path in a playbook task.
    - Supported check mode.
requirements:
	- python >= 2.7
    - cerberus == 1.3.2
'''

EXAMPLES = '''
name: validate variables
vars_schema_validator:
    var: '{{ vars }}'
    schema: schema.yaml
'''

RETURN = '''#'''

import os
import yaml
from ansible.module_utils.basic import AnsibleModule
from cerberus import Validator

def include_constructor(loader, node):
    '''Handler for !include.'''
    root = os.path.split(loader.stream.name)[0]
    filename = os.path.join(root, loader.construct_scalar(node))
    with open(filename, 'r') as f_stream:
        return yaml.safe_load(f_stream)

yaml.add_constructor('!include', include_constructor, yaml.SafeLoader)

def run_module():
    '''Validate the variables.'''
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
                    msg="All custom vaiables are validated."
                )
            else:
                module.fail_json(msg=validator.errors)

        except yaml.YAMLError as err:
            module.fail_json(msg=err)

def main():
    run_module()

if __name__ == '__main__':
    main()
