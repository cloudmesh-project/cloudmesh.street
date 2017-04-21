import numpy as np
import cv2


stop_cascade = cv2.CascadeClassifier('/opencv_workspace/classifier/stopsign_classifier.xml')

cap = cv2.imread('/opencv_workspace/test_data/images/test1.jpg')


gray = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)
stops = stop_cascade.detectMultiScale(
    gray, 
    scaleFactor=1.1, 
    minNeighbors=2
    )

for (x,y,w,h) in stops:
    cv2.rectangle(cap,(x,y),(x+w,y+h),(255,0,0),2)

# show objects on street image
cv2.imwrite('/opencv_workspace/output/streetimage1.jpg', cap)
cv2.destroyAllWindows()
        
   
