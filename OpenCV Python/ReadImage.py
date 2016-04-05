#python program to load image

import cv2
import numpy as np


img = cv2.imread('C:\Users\Devashish\Desktop\dr.jpg',-1)

cv2.imshow("Read Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()