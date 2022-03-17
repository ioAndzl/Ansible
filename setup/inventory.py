"""
.group hosts
[devops]
server1
server2

[db]
server3
server4

[app]
server5
server6
.. launch playbook on a group
ansible app all -m ping

.groups of groups
.group hosts
[devops]
server1
server2

[db]
server3
server4

[app]
server5
server6

[eastzone:children]
devops
db
.. launch playbook on a group of groups
ansible eastzone -m ping


.regular expression in inventory
[devops]
server[1:9]
[db]
server[10:19]
[app]
server[20:29]
[eastzone:children]
devops 
db

.usage of password in inventory file 
[passwordless]
server1
server2

[password]
server3 ansible_ssh_user=andzl ansible_ssh_password=redhat

or

[passwordless]
server1
server2

[password]
server3

[password:vars]
ansible_ssh_user=andzl
ansible_ssh_password=redhat

..usage
ansible -i myinventory all -m command -a "whoami"
"""
