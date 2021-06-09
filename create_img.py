import cv2
import numpy as np
frame  = np.zeros([600,600,3], np.uint8)
# for creating black image

#points used in img
pt1 = (200,100)
pt2 = (100,200)
pt3 = (300,200)
pt4 = (400,100)
pt5 = (500,200)
sq1 = (250,200)
sq2 = (250,400)
rec1 = (150,200)
rec2 = (450,400)

#COLOR 
clr = (0,255,0)


#defined function
def drawline(point1,point2):
    return cv2.line(frame,point1,point2,clr,2)


#make lines on img
drawImg = drawline(pt1,pt2)
drawImg = drawline(pt1,pt3)
drawImg = drawline(pt2,pt3)
drawImg = drawline(pt1,pt4)
drawImg = drawline(pt3,pt5)
drawImg = drawline(pt4,pt5)
drawImg = drawline(pt3,pt5)
drawImg = drawline(sq1,sq2)
drawImg = cv2.rectangle(frame,rec1,rec2,clr,2)


#show the image
cv2.imshow('image', drawImg)
cv2.waitKey()
cv2.destroyAllWindows()
