"""
gathering facts : collect system information of the managed nodes
Usage: setup mudule => ansible_facts variable

.system default facts
ansible all -m setup -a 'filter="ansible_kernel"'

.user defined facts 
..usage 
ansible all -m file -a "path=etc/ansible/facts.d state=directory" --become
..in /tmp/python_version.fact
{
#!/bin/bash
python_ver=$(python3 -version | cut -d' ' -f2)

cat << EOF
{"Python_version":"${python_ver}"}
EOF
}
ansible all -m copy -a "src=/tmp/python_version.fact dest=/etc/ansible/facts.d mode=700 owner=uansible group=uansible" --become
ansible all -m setup -a "filter=ansible_local"
"""
