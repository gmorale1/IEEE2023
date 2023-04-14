import cv2
import argparse

from ultralytics import YOLO
CAM_1 = 1

cam = cv2.VideoCapture(CAM_1)

model = YOLO("C:/Users/edwar/OneDrive/Desktop/repositories/IEEE2023/PI/finyolov8n.pt")

while True:
    ret, frame = cam.read()

    result = model(frame)

    cv2.imshow('finyolov8n', frame)
    if(cv2.waitKey(30) == 27):
        break