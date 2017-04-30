#This code simply reads in a video and outputs the video frames to image files using opencv
def video2image(vpath):
    import cv2
    import numpy as np
    import os

    filelist=[os.path.join(vpath,f) for f in os.listdir(vpath) if f.endswith("mp4")]
    ctr = 1
    newpath = vpath +'img/'
    for vi in filelist:
	    video = cv2.VideoCapture(vi)
	    count = 1
	    while(video.isOpened()):
		check,frame = video.read()
		if (check == False):
		    break
		else:
		    cv2.imwrite(newpath+ str(ctr)+'_'+str(count)+'.jpg',frame)
		    count += 1
    ctr += 1
    video.release()
    return newpath



