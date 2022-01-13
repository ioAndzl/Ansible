"""
.doc 
ansible-doc -l
ansible-doc <module name>

.generic command
ansible [-i INVENTORY] [server] [-m MODULE] {-a MODULE_OPTIONS} 

.usage of a module
ansible all -m shell -a uptime
ansible all -m shell -a "free -m"
..keep module on managed host 
ANSIBLE_KEEP_REMOTE_FILES=1 ansible all -m shell -a "free -m"
..adjust fork parameter
ansible all -m shell -a uptime -f 1
..tranfer file to host
ansible [-i INVENTORY] [server] -m copy -a "src=file_path dest=dest_folder_path"
ansible all -m copy -a "src=/tmp/ctrl_file dest=/home/uansible/"
..add content on a file on host 
ansible all -m copy -a "content='Hello, my name is Aadil' dest=~/ctrl_file"
..download file from host
ansible all -m fetch -a "src=file_path dest=dest_folder_path flat=yes"
ansible all -m fetch -a "src=~/tmpfile dest=~/ flat=yes"
..copy a file on server from the same server
ansible all -m copy -a "src=file_to_copy_path dest=copied_file_path remote_src=yes"
..create file on managed nodes
ansible all -m file -a "path=file_path state=touch"
ansible all -m file -a "path=file_path state=touch mode=755"
..remove file on managed nodes
ansible all -m file -a "path=file_path state=absent"
..create directory on managed nodes
ansible all -m file -a "path=file_path state=directory"
..remove directory on managed nodes
ansible all -m file -a "path=diretory_path state=absent"

.execute a command with root priviledge
ansible all -m command -a "fdisk -l" --become
ansible all -m command -a "fdisk -l" -b
.. if --beocome fails, it is because it is asking for password
ansible all -m command -a "fdisk -l" --become --ask-become-pass

.install a package on managed host
ansible all -m apt -a "name=git state=latest" --become

.execute command as being a different user 
ansible all -m command -a "whoami" --user andzl --ask-pass




"""