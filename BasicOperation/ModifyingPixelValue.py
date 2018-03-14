import cv2
import numpy as np 

img = cv2.imread("ragdoll.jpg")
px = img[100, 100]
print px #[26, 33, 50]

# accessing only blue pixel
blue = img[100, 100, 0]
# green = img[100, 100, 1]
# red = img[100, 100, 2]
print blue

# change pixel value
img[100, 100] = [255, 255, 255]
# change red value
img[100, 100, 2] = 100
print img[100, 100, 2]

# alternative mathod
img.item(20,20,2)
print img[20,20,2]
img.itemset((20,20,2), 99)
img.item(20, 20, 2)
print img[20,20,2]

