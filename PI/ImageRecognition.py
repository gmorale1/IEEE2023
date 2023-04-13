#OpenCV Recognition Test Fall 2022
#Programmer: Gaddiel Morales
#Purpose: Train and recognize an object

import cv2 as cv

#Camera ports
CAM_1 = 0

#get an image from the camera
camera = cv.VideoCapture(CAM_1)
result, image = camera.read()
#for x in image:
#    print(x[0][0])
#    for y in x:
#        x = y
#        for z in y:
            
#img = cv.resize(image, (0,0), fx = 0.5, fy = 0.5)
img = cv.resize(image, (100, 100))
#TODO: display camera picture in window
if result:
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(gray_image, 50, 255, cv.THRESH_BINARY)
    cv.imshow("IEEEImage", binary)
    
    cv.imwrite("IEEEImage.png", binary)
    
    cv.waitKey(0)
    cv.destroyWindow("IEEEImage")
    
else:
    print("No image detected. Please! try again")

#TODO: draw circle on picture

#TODO: Get file of multiple previously recognized objects

#TODO: Put circle on where the object is in the picture




    