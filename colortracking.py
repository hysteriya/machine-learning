import cv2
import imutils

orglow= (0, 100, 100)
orghigh=(179, 255, 255)
cam= cv2.VideoCapture(0)

while True:
    _,img = camera.read()#reading the frame
    frame= imutils.resize(frame, width=600)#resizing
    blur=cv2.GaussianBlur(frame, (11,11),0)#smoothining
    hsv= cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)#bgr to hsv
    mask=cv2.inRange(hsv, orglow, orghigh)#extract the color area
    mask=cv2.erode(mask, None, iterations=2)#remove noises
    mask=cv2.dialate(mask, None, iterations=2)
    cnts= cv2.findContours(mask.copy(), cv.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) [-2]#boundries
    center=None
    if len(cnts)>0: #if theres an obj present
        c= max (cnts, key=cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius>10:
            cv2.circle(frame, (int(x), int(y), int(radius), (0,255,255), 2)#dynamic radis
            cv2.circle(frame, center, 5, (0, 0, 255), -1)#static raduis(identified from moments)
            
            if radius > 250:#obj is far
                print("stop")
            else:
                if(center[0]<150):
                     print("Left")
                elif(center[0]>450):
                    print("Right")
                elif(radius<250):
                    print("Front")
                else:
                    print("Stop")
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
camera.release()
cv2.destroyAllWindows()
        
                    
                
                
                    
                
                
                
                
            
                       
            
    
                       
                            
                 
                 
                      
