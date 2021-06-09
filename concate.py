import cv2
import numpy as np
# load image
pic1 = cv2.imread('black_stone.png')
pic2 = cv2.imread('white-stone.png')
# concate two images horizontally
horiPic = np.concatenate((pic1,pic2),axis=1)

cv2.imshow('Horizontal', horiPic)
cv2.waitKey()
cv2.destroyAllWindows()
# concate two images vertically
VertiPic = np.concatenate((pic1,pic2),axis=0)

cv2.imshow('Vertical', VertiPic)
cv2.waitKey()
cv2.destroyAllWindows()
