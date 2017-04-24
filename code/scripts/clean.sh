#!/bin/bash

# Change Directory for playbook_run:

cd $HOME/github/cloudmesh.street/ansible

#Run ansible playbook:

ansible-playbook env_clean.yaml --ask-sudo-pass -v


