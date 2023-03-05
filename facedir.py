import cv2
import os
hccff_algo_file = "haarcascade_frontalface_default.xml"
hccff = cv2.CascadeClassifier(hccff_algo_file)
print("Loaded hccff algo...")
cam = cv2.VideoCapture(0)
print("Initialised camera...")

directory = "human_face"
subdirectory = "person_name"

path = os.path.join(directory, subdirectory)
cwd = os.getcwd()
print("Path: %s\\%s"%(cwd, path))
abs_path = "%s\\%s"%(cwd, path)

if not os.path.isdir("%s"%(abs_path)):
    print("Directory doesnot exist, creating... %s"%(abs_path))
    os.makedirs(abs_path, exist_ok=True)
else:
    print("Directory already exists, skip creation...")

no_of_pics = 1
(width, height) = (130, 100)

while no_of_pics < 31:
    print("Capturing video...")
    _,img = cam.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    print("Detecting faces...")
    face = hccff.detectMultiScale(gray_img, 1.3, 2)
    print("Faces: ",face)
    for (x,y,w,h) in face:
        print("Each face coordinates to draw rectangle: (X- %s, Y- %s, W- %s, H- %s)"%(x,y,w,h))
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        faceOnlyCords = gray_img[y:y+h, x:x+w]
        resizedImg = cv2.resize(faceOnlyCords, (width, height))
        cv2.imwrite("%s/%s.jpg"%(abs_path, "pic%s"%no_of_pics), faceOnlyCords)
    cv2.imshow("FaceDetection", img)
    key = cv2.waitKey(10)
    if key == 27:
        print("Stopping face recognition")
        break
    no_of_pics += 1
else:
    print("Exiting picture capture after %s clicks"%(no_of_pics))
cam.release()
cv2.destroyAllWindows()
