import numpy as np 
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('ragdoll.jpg', 0)
#b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([]) # to hide tick values on x and y axis

plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show() 

cv2.imshow('bgr image', img)
cv2.imshow('rgb image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()