import cv2

alg="haarcascade_frontalface_default.xml"

haar= cv2.CascadeClassifier(alg)
cam= cv2.VideoCapture(0)
while True:
    _,img=cam.read()
    grayimg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = haar.detectMultiScale(grayimg, 1.3, 4)
    for (x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255,0), 2)
    cv2.imshow("facedection",img)
    key=cv2.waitKey(10)
    if key==27: #esc
        break
cam.release()
cv2.destroyAllWindows()
    
