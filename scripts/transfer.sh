#!/bin/bash

# Change Directory for playbook_run:

cd $HOME/github/cloudmesh.street/ansible

#Clean local output directory before running
rm -r ansible/output

#Run the output data transfer playbook:
ansible-playbook transfer_output_to_local.yaml -i inv --ask-sudo-pass -vvv

