import cv2
import numpy as np 

img = cv2.imread("ragdoll.jpg")
print img.shape #return (rows, columns, channels)

print img.size # number of pixels

print img.dtype # image datatype

# get the cat region of image
cv2.namedWindow('cat', cv2.WINDOW_NORMAL)
cat = img[120:419, 170:480]
cv2.imshow('image', cat)
cv2.waitKey(0)
