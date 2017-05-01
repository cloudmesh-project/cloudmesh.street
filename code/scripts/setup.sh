#!/bin/bash

# Change Directory for playbook_run:

cd $HOME/github/cloudmesh.street/ansible

#Turn off SSH authenticity checking
export ANSIBLE_HOST_KEY_CHECKING=false
	
#Supress warnings
export ANSIBLE_DEPRECATION_WARNINGS=false
export ANSIBLE_COMMAND_WARNINGS=false

#Run ansible playbook:

ansible-playbook -i inventory.txt local_setup.yaml -v


