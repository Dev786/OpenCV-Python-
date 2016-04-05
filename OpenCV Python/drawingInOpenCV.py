import cv2
import numpy as np

img = cv2.imread("C:\Users\Devashish\Desktop\dr.jpg",cv2.IMREAD_COLOR)

#Line
cv2.line(img,(0,0),(200,250),(255,0,0),15)


#rectangle
cv2.rectangle(img,(0,0),(400,400),(0,255,0),10)

#circle
cv2.circle(img,(200,150),20,(0,0,255),-1)


#polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#pts = pts.reshape((-1,1,2))


cv2.polylines(img,[pts],True,(255,255,0),3)


#font
font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img,"Devashish is awesome",(250,250),font,1,(255,0,0),2,cv2.LINE_AA)

cv2.imshow("Image",img)
cv2.waitKey(0)

cv2.destroyAllWindows()