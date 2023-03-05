import cv2
import imutils
img = cv2.imread("imt.jpg")
resizeImg=imutils.resize(img, width=20)
cv2.imwrite("resizedimt.jpg", resizeImg)
