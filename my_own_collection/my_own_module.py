#!/usr/bin/python3

# Copyright: (c) 2024 Your Name
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_file_module

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
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create a file with content
  my_namespace.my_collection.my_file_module:
    path: /tmp/test.txt
    content: "Hello, World!"

- name: Create another file
  my_namespace.my_collection.my_file_module:
    path: /tmp/example.txt
    content: |
      Line 1
      Line 2
      Line 3
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
        # In check mode, just check if file exists and has correct content
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

    # Check if file exists and has the correct content
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

    # Create or update the file if needed
    if need_to_create:
        try:
            # Ensure directory exists
            directory = os.path.dirname(path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            
            # Write content to file
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