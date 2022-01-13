"""
.create user:
useradd user
passwd user

"""

"""
.delete user:
sudo su -
userdel -r user
"""

"""
.create user with repertoire
sudo useradd -m username
.create user with specific repertoire
sudo useradd -m -d /opt/username username
"""

"""
.add a user in the list of sudoers
echo "uansible ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/uansible
"""

"""
.change root password
sudo passwd root
or
sudo -i 
passwd
"""