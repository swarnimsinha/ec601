import cv2
#import numpy as np

while True:
	img = cv2.imread('index.png',0)	#save the image in a variable
	edges = cv2.Canny(img,100,200)	#apply the canny edge filter

	cv2.imshow("source", img)	#show the original image
	k = cv2.waitKey(33)	#delay to handle key presses
	if k == 27:	#if the escape key is pressed, break the loop
		break
	elif k == 32:	#else if space key is pressed
		cv2.imshow("cannyEdge", edges)	#show the canny filter
		#todo - check how canny edge filter actually works
		#apply those filters manually to show the working