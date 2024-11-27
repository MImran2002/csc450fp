import cv2 as cv
import sys
import os
import time

camera = 0
if len(sys.argv) > 1:
    camera = sys.argv[1]
    print(camera)

source = cv.VideoCapture(camera)
print(source)

def face_capture(frame):
    algorithm = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_id = input("enter id of user: ")
    name = input("Enter name: ")
    sample = int(input("Enter how many sample you wish to take: "))

    for f in os.listdir(path):
        os.remove(os.path.join(path, f))
    time.sleep(2)

    count=0
    while True:
        ret,img=frame.read()
        converted_image=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        face=algorithm.detectMultiScale(converted_image,1.3,5)


cv.namedWindow("Camera Pop-up", cv.WINDOW_NORMAL)
while cv.waitKey(2) != 27:
    frame_exist, img_matrix = source.read()
    if frame_exist == False:
        break
    else:
        cv.imshow("Camera Pop-up", img_matrix)
        face_capture(frame)


