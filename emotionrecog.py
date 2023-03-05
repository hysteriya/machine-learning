from facial_emotion_recognition import EmotionRecognition
import cv2

er = EmotionRecognition(device='cpu')
#if gpu device='gpu'
cam = cv2.VideoCapture(0)

while True:
    success, frame = cam.read()
    frame = er.recognise_emotion(frame, return_type='BGR')#can work with rgb too
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
