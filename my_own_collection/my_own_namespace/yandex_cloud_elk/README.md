# my_own_namespace.yandex_cloud_elk

## Description
This collection provides custom Ansible modules for file operations.

## Modules
### my_file_module
Creates a text file on remote host with specified content.

#### Parameters
- `path` (str, required): Path to the file to create
- `content` (str, required): Content to write to the file

#### Examples
```yaml
- name: Create a file
  my_own_namespace.yandex_cloud_elk.my_file_module:
    path: /tmp/myfile.txt
    content: "Hello World"