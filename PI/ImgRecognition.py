import cv2 as cv
from pathlib import Path
path = Path('C:/Users/edwar/OneDrive/Desktop/repositories/IEEE2023/PI/videos/ybox.mp4')
video = cv.VideoCapture('C:/Users/edwar/OneDrive/Desktop/repositories/IEEE2023/PI/videos/ybox.mp4')
if path.is_file():
    print("cheese")
count = 0
success = True
imgPath = "C:/Users/edwar/OneDrive/Desktop/repositories/IEEE2023/PI/img/ybox/"
while success:
    success, image = video.read()
    print(count)
    #print(success)
    if not success: 
        break
    cv.imwrite(imgPath+"frame"+str(count)+".jpg", image)
    count += 1

video.release()
