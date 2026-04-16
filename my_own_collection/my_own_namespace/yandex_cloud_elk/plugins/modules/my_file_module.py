#!/usr/bin/python3

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module
short_description: Module to create a text file on remote host
version_added: "1.0.0"
description: This module creates a text file on the remote host with specified content.
options:
    path:
        description: Path to the file to create on remote host.
        required: true
        type: str
    content:
        description: Content to write to the file.
        required: true
        type: str
author:
    - Your Name
'''

EXAMPLES = r'''
- name: Create a file with content
  my_own_module:
    path: /tmp/test.txt
    content: "Hello, World!"
'''

RETURN = r'''
path:
    description: Path to the file that was created/checked.
    type: str
    returned: always
    sample: '/tmp/test.txt'
content:
    description: Content that was written to the file.
    type: str
    returned: always
    sample: 'Hello, World!'
changed:
    description: Whether the file was created or modified.
    type: bool
    returned: always
    sample: true
'''

import os
from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']
    
    result['path'] = path
    result['content'] = content

    if module.check_mode:
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    existing_content = f.read()
                if existing_content != content:
                    result['changed'] = True
            except:
                result['changed'] = True
        else:
            result['changed'] = True
        module.exit_json(**result)

    need_to_create = True
    
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                existing_content = f.read()
            if existing_content == content:
                need_to_create = False
            else:
                need_to_create = True
        except Exception as e:
            module.fail_json(msg=f"Error reading file {path}: {str(e)}", **result)
    else:
        need_to_create = True

    if need_to_create:
        try:
            directory = os.path.dirname(path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            
            with open(path, 'w') as f:
                f.write(content)
            result['changed'] = True
        except Exception as e:
            module.fail_json(msg=f"Error writing to file {path}: {str(e)}", **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()