import cv2
import time
import imutils

cam= cv2.VideoCapture(0)
time.sleep(1)

firstFrame=None
area=500
while True:
    _,img = cam.read()
    text="normal"
    img= imutils.resize(img, width=500)
    grayImg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurImg= cv2.GaussianBlur(grayImg, (21,21), 0)
    if firstFrame is None:
        firstFrame= blurImg
        continue
    imgdiff=cv2.absdiff(firstFrame, blurImg)
    thresh=cv2.threshold(imgdiff, 25, 255, cv2.THRESH_BINARY)[1]
    dil= cv2.dilate(thresh, None, iterations=2)
    cnts= cv2.findContours(dil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts= imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c)<area:
            continue
        (x, y, w, h)= cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        text= "moving obj detected"
    print(text)
    cv2.putText(img, text, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),2)
    
                      
    
    
    cv2.imshow("camfeed", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
