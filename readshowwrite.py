import cv2

img= cv2.imread("a.png")

cv2.imshow("a",img)
cv2.imwrite("a2.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
