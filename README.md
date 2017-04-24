### STREET-SIGNS DETECTION in VIDEO STREAM OVER SPARK-HADOOP CLUSTER

#### STEP 1: Clone or download cloudmesh.street repository to local machine

    git clone https://github.com/cloudmesh/cloudmesh.street.git 

#### STEP 2: After getting local copy of the git repository, Go to directory './code/scripts'

#### STEP 3: To install ansible, cloudmesh client for the first-time:
   (Note: Skip 3.1 if already installed )
##### 3.1 Run the script local_setup.sh from ./code/scripts folder:

    . setup.sh 

The above script when runs uses playbook--> ansible/local_setup.yaml

##### 3.2 Run the script configure.sh from  ./code/scripts folder:
    
    . configure.sh

The above script when runs uses playbook--> ansible/cloud_config.yaml and ask for user input for following fields:
   (Note: Values in [] are default values just press ENTER if requires default configuration) 
    
    	enter the cloudname[chameleon]:
    	enter the key_name,preferably cloud_username[TBD]:
	

##### 3.3 Run the script deploy.sh from  ./code/scripts folder:
    
    . deploy.sh

The above script when runs ,uses playbook--> ansible/hadoop_deploy.yaml and ask for user input for following fields:
  (Note: Values in [] are default values just press ENTER if requires default configuration)    
    enter image_name[CC-Ubuntu14.04]:
    enter the no. of nodes[3]:
    enter the flavor requried[m1.medium]:  
    enter the addons required[spark pig]:
    
##### 3.4 Run the script opencv_setup.sh from  ./code/scripts folder:
    
    . opencv_setup.sh

The above script when runs ,uses playbook--> ansible/opencv_setup.yaml

##### 3.5 Run the script sifn_detection.sh from  ./code/scripts folder:
    
    . sign_detection.sh

The above script when runs ,uses playbook--> ansible/sign_detection.yaml

##### 3.6 Run the script transfer.sh from  ./code/scripts folder:
    
    . transfer.sh

The above script when runs ,uses playbook--> ansible/transfer_output_to_local.yaml
    
##### 3.7 Run the script clean.sh from  ./code/scripts folder:
    
    . clean.sh
    
The above script when runs ,uses playbook--> env_clean.yaml
    

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

##### A.1.3 Edit the configuration for the active cloud below it from the list(kilo/chameleon/jestream/..), the entry with < > should be customized as per your credentials.

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
