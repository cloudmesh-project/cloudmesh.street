### STREET-SIGNS DETECTION in VIDEO STREAM OVER SPARK-HADOOP CLUSTER

#### STEP 1: Clone or download cloudmesh.street repository to local machine

    git clone https://github.com/cloudmesh/cloudmesh.street.git 

#### STEP 2: After getting local copy, Go to directory 'ansible'

#### STEP 3: To install ansible, cloudmesh client for the first-time run script 'install_ansible_cloudmesh_client.sh' with following comnmand:

./install_ansible_cloudmesh_client.sh

#### STEP 4
##### 4.1 Open ~/.cloudmesh/cloudmesh.yaml and edit the following sections, edit <''>/ <TBD> in the file correct credentials:

     profile:
           firstname: <first name>
           lastname: <last name>
           email: <email id>
           user: <chameleon/jetsream/other cloud username>

##### 4.2 Change the entry of active cloud for the one you need,For e.g. chameleon cloud as shown below:

    active:
      - chameleon
    clouds:
      ...

##### 4.3 Edit the configuration for the active cloud below it from the list(kilo/chameleon/jestream/..), the entry with < > should be customized as per your credentials.

Chameleon Example:

    credentials:
    OS_PASSWORD: <enter your chameleon cloud password here>
    OS_TENANT_NAME: CH-818664
    OS_TENANT_ID: CH-818664
    OS_PROJECT_NAME: CH-818664
    OS_USERNAME: <username>

##### 4.4 Also change default OS image and flavor as per requirement under cloud configuration:

    default:
            flavor: m1.medium
            image: CC-Ubuntu14.04

#### STEP 5: Run the cloud_cluster_setup.yaml 



#### STEP 6: Run the 'host_edit.sh' script to update hosts with IPS of all three deployed VMS: 
  (Note: On the cluster, first node becomes master)

    ```sh
    ./hosts_edit.sh
    ```

#### STEP7: Run 'hadoop_deploy' playbook to deploy hadoop with addons spark,pig:



#### STEP8: 




#### STEP9:





## Appendix:

### Manual steps for running the spark job over cluster

#### Setup OpenCV workspace on master

#### Cleanup of deployment on cluster
