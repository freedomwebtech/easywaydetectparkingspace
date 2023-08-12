import cv2
import cvlib as cv
import cvzone
import numpy as np
import time
from cvlib.object_detection import draw_bbox
from tracker import*
cap=cv2.VideoCapture(r"C:\Users\freed\ytfinalvideos\parkinspace.avi")
tracker=Tracker()
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

count=0
while True:
    ret,frame=cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame=cv2.resize(frame,(1020,500))
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)
    cv2.imshow("RGB",frame)
   
#    time.sleep(0.1)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
   
