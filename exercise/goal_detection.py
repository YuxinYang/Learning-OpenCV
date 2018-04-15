import cv2
import sys
import numpy as np
from os.path import isfile

def harrisCorner_operation(gray):
	gray = np.float32(gray)
	dst = cv2.cornerHarris(gray,2,3,0.04)

	#result is dilated for marking the corners, not important
	dst = cv2.dilate(dst,None)
	# Threshold for an optimal value, it may vary depending on the image.
	img[dst>0.01*dst.max()]=[0,0,255]
	cv2.imwrite('harrCorner.jpg',img)

def sobel_operation(img):
	laplacian = cv2.Laplacian(img, cv2.CV_64F)
	sobelx = cv2.Sobel(laplacian, cv2.CV_64F, 1, 0, ksize=5)
	sobely = cv2.Sobel(laplacian, cv2.CV_64F, 0, 1, ksize=5)
	
	cv2.imwrite('laplacian.jpg', laplacian)
	cv2.imwrite('sobelx.jpg', sobelx)
	cv2.imwrite('sobely.jpg', sobely)

def sift_operation(gray):
	sift = cv2.SIFT()
	kp = sift.detect(gray,None)
	img1=cv2.drawKeypoints(gray,kp)
	cv2.imwrite('sift1_keypoints.jpg',img1)

	img2=cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	cv2.imwrite('sift2_keypoints.jpg',img2)


if __name__ == '__main__':
	if len(sys.argv) == 2 and isfile(sys.argv[1]):
		filename = sys.argv[1]
		print "processing single image file: ", filename
		img = cv2.imread(filename)
		img = cv2.medianBlur(img, 7) # erase noise
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		sobel_operation(gray)
		harrisCorner_operation(gray)
		sift_operation(gray)
	else:
		print __doc__
		print "wrong number/type of arguments."
		sys.exit(1)