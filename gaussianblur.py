import cv2

img = cv2.imread("a.png")
gaussianBlurImg= cv2.GaussianBlur(img, (21, 21), 0) #gaussianblur is mostly odd
cv2.imwrite("gaussian.jpg", gaussianBlurImg)
cv2.imshow("gaussian",gaussianBlurImg)
