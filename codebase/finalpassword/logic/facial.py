import cv2 as cv
import sys

camera = 0
if len(sys.argv) > 1:
    camera = sys.argv[1]
    print(camera)

source = cv.VideoCapture(camera)
print(source)

cv.namedWindow("Camera Pop-up", cv.WINDOW_NORMAL)
while cv.waitKey(2) != 27:
    frame_exist, img_matrix = source.read()
    if frame_exist == False:
        break
    else:
        cv.imshow("Camera Pop-up", img_matrix)
        


