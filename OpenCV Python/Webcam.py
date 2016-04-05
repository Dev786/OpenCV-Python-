import cv2
import numpy as np


cap = cv2.VideoCapture(0)


while True:
    ret,frame = cap.read()
    cv2.imshow("Video",frame)

    if(cv2.waitKey(1)==27): #27 is for esc key
        break


cap.release()
cv2.destroyAllWindows()