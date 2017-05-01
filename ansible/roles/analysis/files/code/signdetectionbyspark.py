from __future__ import print_function
import imutils
from imutils import paths
from pyspark import SparkContext, SparkConf
import cv2
import numpy
import sys
from video2image import video2image

def process_images(image):
		import cv2
		stop_cascade = cv2.CascadeClassifier('/opencv_workspace/classifier/stopsign_classifier.xml')
		test = cv2.imread(image)
		gray = cv2.cvtColor(test,cv2.COLOR_BGR2GRAY)
		stops = stop_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
		for (x,y,w,h) in stops:
			cv2.rectangle(test,(x,y),(x+w,y+h),(255,0,0),2)
		return test

if __name__== "__main__":
	if(len(sys.argv)!=3):
		print("Usage: streetsign input output")
		exit(-1)
		
	conf = SparkConf().setAppName("Street Sign")
	conf = conf.set("spark.executor.heartbeatInterval","3600s")
	conf = conf.set("spark.rpc.askTimeout","700s")
	sc = SparkContext(conf = conf)
	imageDir = sys.argv[1]
	outputDir = sys.argv[2]
        print(imageDir)
        print(imageDir)
        if (imageDir != '/opencv_workspace/test_data/images/'):
                imageDir = video2image(imageDir)
                print(imageDir)
	pd = sc.parallelize(paths.list_images(imageDir),60)
	pdc = pd.map(process_images)
	result = pdc.collect()
        
	count = 1
	for img in result:
		# save the output to jpg files
		cv2.imwrite(outputDir+str(count)+'.jpg',img)
                count = count+1
		if (count >len(result)):
		   break
