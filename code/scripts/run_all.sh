#!/bin/bash

echo "Setting up local machine(ansible,cloudmesh,packages)" 
#./setup.sh 

echo "cloudmesh and cloud setup" 
./configure.sh 

echo "deploying hadoop with spark over cluster" 
./deploy.sh 

echo "opencv setup over cluster" 
./opencv_setup.sh

echo "street sign detection program over spark" 
./sign_detection.sh

echo "data transfer between remote and local machine" 
./transfer.sh

echo "environment clean" 
#./clean.sh

