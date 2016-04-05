import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('M','J','P','G') #if MJPG does not work try (*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20,(640,480))

while True:
    ret,frame = cap.read()
    cv2.imshow("Frame",frame)
    out.write(frame)
    if(cv2.waitKey(1)==27): #27 is esc key
        break

cap.release()
out.release()
cv2.destroyAllWindows()