## STOP SIGN DETECTION IN IMAGE AND VIDEO STREAMS USING SPARK

### PROJECT REPORT - https://github.com/cloudmesh/sp17-i524/blob/master/project/S17-IR-P003/report/report.pdf

#### STEP 1: Clone or download cloudmesh.street repository to local machine

    git clone https://github.com/cloudmesh/cloudmesh.street.git 

#### STEP 2.1: UPDATE THE USER PREFERENCES
After getting local copy of the git repository, Go to directory "./ansible"
    UPDATE THE FOLLOWING VARIABLES <TBD values> IN "user_vars.yaml"
	
	---
	###########################################################
	#Variables for execution of complete package

	#EDIT FOLLOWING DETAILS AS PER REQUIREMENT

	##############CLOUDMESH SETTINGS###########################
	#cloud: "chameleon" or "jetstream"
	cloud: <TBD>
	#username: "cloudmesh username as key_name"
	username: <TBD>
	############HADOOP CLUSTER SETTINGS########################
	#Chameleon image_name: CC-Ubuntu14.04
	#jetstream image_name: ubuntu-14.04-trusty-server-cloudimg
	#flavor: m1.small, m1.medium, m1.large[preferred: m1.medium]
	#addons: spark pig hive

	image_name: <TBD>
	count: <TBD>
	flavor: <TBD>
	addons: <TBD>

	###########################################################

#### For e.g.: 

	---
	############################################################
	#Variables for execution of complete package

	#EDIT FOLLOWING DETAILS AS PER REQUIREMENT

	##############CLOUDMESH SETTINGS############################
	#cloud: "chameleon" or "jetstream"
	cloud: "chameleon"
	#username: "cloudmesh username as key_name"
	username: "rraghata"
	############HADOOP CLUSTER SETTINGS#########################
	#Chameleon image_name: CC-Ubuntu14.04
	#jetstream image_name: ubuntu-14.04-trusty-server-cloudimg
	#flavor: m1.small, m1.medium, m1.large [preferred: m1.medium]
	#addons: spark pig hive


	image_name: "CC-Ubuntu14.04"
	count: "6"
	flavor: "m1.medium"
	addons: "spark"

	############################################################

#### STEP 2.2: CHANGE WORKING DIRECTORY
Go to directory '/cloudmesh.street/code/scripts'

#### STEP 3: To install ansible, cloudmesh client for the first-time and run complete package run following script:

	. run_all.sh
	
#### STEP 3: ANSIBLE PLAYBOOK EXECUTION BREAKDOWN 
{Note: Skip 3.1 if already installed )

##### 3.1 Run the script local_setup.sh for ansible and cloudmesh setup on local machine:

    . setup.sh 

The above script when runs uses playbook--> ansible/local_setup.yaml
Edit the cloudmesh.yaml file as  per requirements [DETAILS GIVEN IN APPENDIX]

##### 3.2 Run the script configure.sh for cloudmesh and cloud configuration:
    
    . configure.sh

The above script when runs uses playbook--> ansible/cloud_config.yaml

##### 3.3 Run the script deploy.sh to hadoop-spark cluster:
    
    . deploy.sh

The above script when runs ,uses playbook--> ansible/hadoop_deploy.yaml

##### 3.4 Run the script opencv_setup.sh for environment setup over cloud cluster for opencv and pyspark:
    
    . opencv_setup.sh

The above script when runs ,uses playbook--> ansible/opencv_setup.yaml

##### 3.5 Run the script sign_detection.sh to perform the sign detection analysis over cloud spark cluster:
    
    . sign_detection.sh

The above script when runs ,uses playbook--> ansible/sign_detection.yaml

###### DEFAULT: 
The images dataset as well as sample video are present in project directory [Details given in Appendix below], the default program performs sign detection on images.

To perform video analysis, Update the following file for last task:

	cloudmesh.street/ansible/roles/analysis/tasks/main.yml

with
	
	su - hadoop -c "spark-submit --master yarn --deploy-mode client --executor-memory 1g --driver-memory 2g --name signdetection --conf "spark.app.id=signdetection" /opencv_workspace/code/signdetectionbyspark.py /opencv_workspace/test_data/videos/ /opencv_workspace/output/"
	
NOTE: You might run in to memory issues if you use m1.small flavors for cluster creation, since the  jobs need a minimum of medium flavor to run. For video, m1.large flavor is preferable for spark computing.
##### 3.6 Run the script transfer.sh to get the output from remote vms(cloud) to local machine for visual confirmation:
    
    . transfer.sh

The above script when runs ,uses playbook--> ansible/transfer_output_to_local.yaml

The output gets stored at "cloudmesh.street/ansible/output" 
   
##### 3.7 Run the script clean.sh to clean the environment:
    
    . clean.sh
    
The above script when runs ,uses playbook--> env_clean.yaml
It deletes all the VMS, undefines all the clusters, delete the output directory and deletes the stacks.
 
##### 4. BENCHMARK
##### 4.1 UPDATE the ./ansible/user_vars.yaml with preferences
##### 4.2 GO TO Directory ./benchmark and run below script:

	. benchmark.sh
	
The above script runs all the scripts[from ../code/scripts] with output in "./benchmark/benchmark_time" file for every script


## Appendix:
#### A.1 Use of Cloudmesh_client

##### A.1.1 Edit ~/.cloudmesh/cloudmesh.yaml for following sections, edit <''>/ <TBD> in the file correct credentials:

	   profile:
		  firstname: <first name>
		  lastname: <last name>
		  email: <email id>
		  user: <chameleon/jetsream/other cloud username>

##### A.1.2 Change the entry of active cloud for the one you need,For e.g. chameleon cloud as shown below

    active:
      - chameleon
    clouds:
      ...

##### A.1.3 Edit the configuration for the active cloud below it from the list(kilo/chameleon/jestream/..), the entry with <TBD> should be customized as per your credentials.

Chameleon Example:

    credentials:
    OS_PASSWORD: <enter your chameleon cloud password here>
    OS_TENANT_NAME: CH-818664
    OS_TENANT_ID: CH-818664
    OS_PROJECT_NAME: CH-818664
    OS_USERNAME: <username>

##### A.1.4 Also change default OS image and flavor as per requirement under cloud configuration:

    default:
            flavor: m1.medium
            image: CC-Ubuntu14.04
#### A.2 DATA
##### A.2.1 Test Data has been provided in "ansible/roles/analysis/files/test_data/"
Following directories are included as sample test-data:

	./images/ - 50 images dataset
	./videos/ - 1 video stop_video_1.mp4 (2 sec) 
Note: Currently, code supports mp4 video files only. 
#### A.3 CLASSIFIER
"STOP SIGN CLASSIFIER" has been provided in "ansible/roles/analysis/files/classifier/"
##### A.3.1 For testing,only one classifier-"STOP SIGN" has been used. 
Multiple classifiers can be added to the directory if you have.

### A.3.2 Above classifier was taken from <https://github.com/markgaynor/stopsigns/tree/master/classifier>. 

