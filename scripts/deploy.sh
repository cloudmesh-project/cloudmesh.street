#!/bin/bash

# Change Directory for playbook_run:

cd $HOME/github/cloudmesh.street/ansible

#clean the inventory
echo '' > inv

#Run ansible playbook:

ansible-playbook hadoop_deploy.yaml --ask-sudo-pass -v

rm $HOME/.ssh/known_hosts
touch $HOME/.ssh/known_hosts
