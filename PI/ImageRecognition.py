#OpenCV Recognition Test Fall 2022
#Programmer: Gaddiel Morales
#Purpose: Train and recognize an object

from cv2 import *

#Camera ports
CAM_1 = 0

#get an image from the camera
camera = VideoCapture(CAM_1)
result, image = camera.read()
print(image)
#TODO: display camera picture in window
if result:
    gray_image = cvtColor(image, COLOR_BGR2GRAY)
    (thresh, binary) = threshold(gray_image, 50, 255, THRESH_BINARY)
    imshow("IEEEImage", binary)
    
    imwrite("IEEEImage.png", binary)
    
    waitKey(0)
    destroyWindow("IEEEImage")
    
else:
    print("No image detected. Please! try again")

#TODO: draw circle on picture

#TODO: Get file of multiple previously recognized objects

#TODO: Put circle on where the object is in the picture




    