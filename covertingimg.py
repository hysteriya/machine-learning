import cv2
img= cv2.imread("a.png")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("grayImage.png", grayImg) //savesimg
cv2.imshow("ori", img)
cv2.imshow("grayImage", grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
