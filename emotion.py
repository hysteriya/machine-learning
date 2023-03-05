from facial_emotion_recognition import EmotionRecognition

import cv2
er= EmotionRecognition(device='cpu')
cam= cv2.VideoCapture(0)
text= "severely depressed"
while True:
    (_, frame)=cam.read()
    cv2.putText(frame, text, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),2)
    frame=er.recognise_emotion(frame, return_type='BGR')
    cv2.imshow('frame', frame)
    key= cv2.waitKey(1)
    if key==27:
        break

cam.release()
cv2.destroyAllWindows()
