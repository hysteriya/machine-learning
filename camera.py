import cv2
import time

cam= cv2.VideoCapture(0) #primary camera-0
time.sleep(1)
while True: #infinite loop
    _,img= cam.read()
    cv2.imshow("camfeed", img)
    key=cv2.waitKey(1)&0xFF
    if key == ord ("q"):
        break

cam.release()
cv2.destroyAllWindows()
