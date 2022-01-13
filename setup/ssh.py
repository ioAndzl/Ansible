"""
ssh-keygen -t ecdsa -b 521
ssh-keygen -t ecdsa -b 521 -f /home/.ssh/myprivatekey #specify output location

#sur le serveur distant
vim /home/user/.ssh/authorized_keys
ou 
ssh-copy-id -i /home/.ssh/myprivatekey user@remotehost

remarque: on peut rajouter dans les fichiers from="10.0.0.2"

#utilisation de la cle
ssh -i privatekey_path user@remotehost

##en utilisant un agent 
-check si agent tourne
ps -p $SSH_AGENT_PID
-lancement d'un agent
eval `ssh-agent`
-ajout de la cle à l'agent
ssh-add
-check de l'ajout de la clé à l'agent
ssh-add -l


#ajouter un config file dans ~/.ssh/
#AWS Servor
HOST aws
   HostName ec2-35-180-29-233.eu-west-3.compute.amazonaws.com
   User ubuntu
   IdentityFile ~/.ssh/AWS.pem
   Port 22
   Loglevel INFO
   Compression yes
   ForwardAgent yes
   ForwardX11 yes
"""

"""
ping: ansible -i "aws," all -m ping 
"""