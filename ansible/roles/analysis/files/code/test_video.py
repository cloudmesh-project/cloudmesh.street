import numpy as np
import cv2

stop_cascade = cv2.CascadeClassifier('stopsign_classifier.xml')

cap = cv2.VideoCapture("stop_video.mp4")
pic_num=1
while (cap.isOpened()):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stops = stop_cascade.detectMultiScale(gray,scaleFactor=1.4, minNeighbors=3)
    
    # add this
    for (x,y,w,h) in stops:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

    #cv2.imshow('img',img)
    cv2.imwrite('output'+str(pic_num)+'.jpg',img)
    pic_num+=1
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
