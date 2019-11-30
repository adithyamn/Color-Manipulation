import cv2
import numpy as np

def dum(x):
	pass
capture = cv2.VideoCapture(0);

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0 , 255 , dum)
cv2.createTrackbar("LS", "Tracking", 0 , 255 , dum)
cv2.createTrackbar("LV", "Tracking", 0 , 255 , dum) 
cv2.createTrackbar("UH", "Tracking", 255 , 255 , dum)
cv2.createTrackbar("US", "Tracking", 255 , 255 , dum)
cv2.createTrackbar("UV", "Tracking", 255 , 255 , dum)


while True:
	#frm = cv2.imread('imagenamehere')
	_, frm = capture.read()

	hsv = cv2.cvtColor(frm, cv2.COLOR_BGR2HSV)
	lh = cv2.getTrackbarPos("LH", "Tracking")
	ls =cv2.getTrackbarPos("LS", "Tracking")
	lv = cv2.getTrackbarPos("LV", "Tracking")
	uh =cv2.getTrackbarPos("UH", "Tracking")
	us = cv2.getTrackbarPos("US", "Tracking")
	uv =cv2.getTrackbarPos("UV", "Tracking")

	lowb = np.array([lh,ls,lv])
	highb = np.array([uh,us,uv])
	det = cv2.inRange(hsv, lowb, highb)

	res = cv2.bitwise_and(frm, frm, mask=det)
	cv2.imshow("frame", frm)
	cv2.imshow("Mask", det)
	cv2.imshow("res", res)

	key = cv2.waitKey(1)
	if key == 27:
		break
capture.release()
cv2.destroyAllWindows()