import cv2
img= cv2.imread("a.png")

gryimg= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresimg= cv2.threshold(gryimg, 120, 255, cv2.THRESH_BINARY)[1]
#var=cv2.threshold(src, threshold, max value, binary type)[1]

cv2.imwrite("thresholdimg.png", thresimg)
cv2.imshow("t", thresimg)
