import cv2
#import numpy as np
canny = 'Canny Image'

# Initialize window to show
cv2.namedWindow(canny)

# this function is needed for the createTrackbar step downstream
def nothing(x):
    pass

# add a threshold slider
th1 = 'threshold1'
cv2.createTrackbar(th1, canny, 0, 255, nothing)
th2 = 'threshold2'
cv2.createTrackbar(th2, canny, 0, 255, nothing)

while True:
	s = cv2.getTrackbarPos(th1, canny)
	t = cv2.getTrackbarPos(th2, canny)

    # get the current position of the tracker

	img = cv2.imread('index.png',0)	#save the image in a variable
	edges = cv2.Canny(img,s,t)	#apply the canny edge filter

	cv2.imshow(canny, edges)	#show the canny filtered image

	k = cv2.waitKey(33)	#delay to handle key presses
	if k == 27:	#if the escape key is pressed, break the loop
		break
	elif k == 32:	#else if space key is pressed
		cv2.imshow("Original Image", img)	#show the original image