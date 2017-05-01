#!/bin/bash
echo ' ' >> benchmark_time
echo ' ' >> benchmark_time
echo 'Benchmark' >> benchmark_time

echo Benchmark 1
echo "Time for local machine setup(ansible,cloudmesh,packages)" 
start=`date +%s`
#. ../code/scripts/setup.sh 
end=`date +%s`
time_for_local_setup=$((end-start))
echo $time_for_local_setup
echo  time_for_local_setup $time_for_local_setup >> ../benchmark/benchmark_time

echo Benchmark 2
echo "Time for cloudmesh and cloud setup(default)" 
start=`date +%s`
. ../code/scripts/configure.sh 
end=`date +%s`
time_for_cloud_setup=$((end-start))
echo $time_for_cloud_setup
echo  time_for_cloud_setup $time_for_cloud_setup >> ../benchmark/benchmark_time

echo Benchmark 3
echo "Time for deploying hadoop with spark over cluster" 
start=`date +%s`
. ../code/scripts/deploy.sh 
end=`date +%s`
time_for_hadoop_deploy=$((end-start))
echo $time_for_hadoop_deploy
echo  time_for_hadoop_deploy $time_for_hadoop_deploy >> ../benchmark/benchmark_time

echo Benchmark 4
echo "Time for opencv setup over cluster" 

start=`date +%s`
. ../code/scripts/opencv_setup.sh
end=`date +%s`
time_for_opencv_setup=$((end-start))
echo $time_for_opencv_setup
echo  time_for_opencv_setup $time_for_opencv_setup >> ../benchmark/benchmark_time

echo Benchmark 5
echo "Time for street sign detection program over spark" 

start=`date +%s`
. ../code/scripts/sign_detection.sh
end=`date +%s`
time_for_sign_detection=$((end-start))
echo $time_for_sign_detection
echo  time_for_sign_detection $time_for_sign_detection >> ../benchmark/benchmark_time

echo Benchmark 6
echo "Time for data transfer between remote and local machine" 
start=`date +%s`
. ../code/scripts/transfer.sh
end=`date +%s`
time_for_data_transfer=$((end-start))
echo $time_for_data_transfer
echo time_for_data_transfer $time_for_data_transfer >> ../benchmark/benchmark_time

#Time for env clean up
echo Benchmark 7
echo "Time for environment clean" 
start=`date +%s`
#. ../code/scripts/clean.sh
end=`date +%s`
time_for_clean_up=$((end-start))
echo $time_for_clean_up
echo time_for_env_cleanup $time_for_clean_up >> ../benchmark/benchmark_time
