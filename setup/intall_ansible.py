"""
installation:

from binary:

git clone https://github.com/ansible/ansible.git
cd ansible
source ./hacking/env-setup
sudo apt install python-pip
pip install --user -r ./requirements.txt
echo "127.0.0.1" > ~/ansible_hosts
export ANSIBLE_INVENTORY=~/ansible_hosts
ansible all -m ping --ask-pass

from pip:cd

sudo apt install python3-pip
pip3 install ansible 

from linux package:

sudo apt install ansible 
"""

"""
change python interpreter
ansible_python_interpreter=/usr/bin/python3
"""

"""
installation python à distance
ansible myhost -- become -m raw -a "yum install -y python3"
"""

"""
connection to amazon host:
~/ioandzl/AWS
ssh -i "AWS.pem" ubuntu@ec2-35-180-29-233.eu-west-3.compute.amazonaws.com
"""

"""
ansible -i "aws," all -m ping
"""