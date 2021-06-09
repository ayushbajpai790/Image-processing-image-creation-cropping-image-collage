import cv2
#read two different image
pic1 = cv2.imread('black_stone.png') 
pic2 = cv2.imread('white-stone.png')
cv2.imshow('pic1', pic1)
cv2.imshow('pic2', pic2)
cv2.waitKey()
cv2.destroyAllWindows()
cp1 = pic1[150:350,250:550]    #black
pic2[180:380,50:350] = cp1
cv2.imshow('pic2', pic2)
cv2.waitKey()
cv2.destroyAllWindows()
pic1 = cv2.imread('black_stone.png') 
pic2 = cv2.imread('white-stone.png')
cp2 = pic2[180:380,50:350]    #white
pic1[150:350,250:550]= cp2
cv2.imshow('pic1', pic1)
cv2.waitKey()
cv2.destroyAllWindows()
