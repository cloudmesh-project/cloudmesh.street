from __future__ import print_function
import imutils
from imutils import paths
from pyspark import SparkContext, SparkConf
import cv2
import matplotlib.pyplot as plt
import numpy
import sys

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
	
	sc = SparkContext(conf = conf)
	imageDir = sys.argv[1]
	outputDir = sys.argv[2]
        #print(imageDir)
        #print(outputDir)
        #print(paths.list_images(imageDir))       
	pd = sc.parallelize(paths.list_images(imageDir))
	pdc = pd.map(process_images)
	result = pdc.collect()
	count = 1
	for img in result:
		# show objects on street image
		#plt.figure()
	        #plt.axis("off")
                #plt.imsave(outputDir+str(count)+'.jpg',cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
		cv2.imwrite(outputDir+str(count)+'.jpg',img)
                count = count+1
		if count == 5
			exit(0)
