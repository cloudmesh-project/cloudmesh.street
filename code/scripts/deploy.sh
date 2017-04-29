#!/bin/bash

# Change Directory for playbook_run:

cd $HOME/github/cloudmesh.street/ansible

#Turn off SSH authenticity checking
export ANSIBLE_HOST_KEY_CHECKING=false
	
#Supress warnings
export ANSIBLE_DEPRECATION_WARNINGS=false
export ANSIBLE_COMMAND_WARNINGS=false

#clean the inventory
echo '' > inv

#Run ansible playbook:

ansible-playbook hadoop_deploy.yaml -v
rm $HOME/.ssh/known_hosts
touch $HOME/.ssh/known_hosts
