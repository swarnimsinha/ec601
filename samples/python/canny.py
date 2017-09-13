import cv2
import numpy as np

while True:
	img = cv2.imread('index.png',0)
	edges = cv2.Canny(img,100,200)

	cv2.imshow("source", img)
	k = cv2.waitKey(33)
	if k == 27:
		break
	elif k == 32:
		cv2.imshow("cannyEdge", edges)