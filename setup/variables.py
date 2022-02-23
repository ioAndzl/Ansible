"""
.there are several types of variables:
    -special variables
    -inventory variables
    -host variables
    -group vaiables
    -facts and local facts
    -connection variables

.variable precedence
(Lowest)
role defaults
inventory file / script group vars 2
inventory group_vars/all
playbook group_vars/all
inventory group_vars/*
playbook group_vars/*
inventory file or script host vars
inventory host_vars/*
playbook host_vars/*
host facts / cached set_facts
play vars
play vars_prompt
play vars_files
role vars (role/vars/main.yml)
block vars (only for task in block)
task vars (only for tasks)
include_vars
set_facts / registered vars
role / include role vars
include params
extra vars

.built-in variables
hostvars : dict {hostnames:{varnames:varvalues}}
inventory_hostname: name of current host known by ansible
group_names : list of groups that the urrent host is member of
groups {"group":[hosts]}
play_hosts : hostname active in the play
ansible_version

.variables in inventory
..host variables
server1
server2 http_port=8080 pkg=httpd
server3
..usage in a playbook
---
  - name:  Verifying host variable
    hosts: server2
    tasks:
    - name: Testing first variable (http_port)
      debug: 
        msg: "The HTTP PORT is {{ http_port }}"
    - name: Testing second variable (pkg)
      debug:
        msg: "The HTTP PORT is {{ pkg }}"
ansible-playbook host_vars.yml

..group variables
[db:vars]
http_port=8080 
pkg=httpd
..usage in a playbook
---
  - name:  Verifying host variable
    hosts: db
    tasks:
    - name: Testing first variable (http_port)
      debug: 
        msg: "The HTTP PORT is {{ http_port }}"
    - name: Testing second variable (pkg)
      debug:
        msg: "The HTTP PORT is {{ pkg }}"
ansible-playbook host_vars.yml
...possible to define group variable and to use the group name as host

..use directly variable in playbook 
vars:
  username: aadil 

..use variable in command line
ansible-playbook var_cmd_line.yml -e myvar=varname


.set_facts for defining variable dynamically:
..see set_fact.yml in lab_ansible

.prompt var
.. see prompt_var.yml

.var from YAML file


"""