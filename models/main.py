import math
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cvzone
from ultralytics import YOLO
import cv2
from playsound import playsound
from sort import Sort
import numpy as np


#results = model('image.png',show=True)
#cv2.waitKey(0)
num_people = 0
cap = cv2.VideoCapture('Train.mp4')
cap.set(3,1280)
cap.set(4,720)
model = YOLO('yolov8n.pt')
detected_people = 0

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]
tracker = Sort()

while True:
    success, img = cap.read()
    results = model(img,stream=True)

    dets = []
    for r in results:
        boxes = r.boxes

        for box in boxes:

            x1,y1,x2,y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1),int(y1),int(x2),int(y2)

            w,h = x2-x1, y2-y1


            conf = math.ceil((box.conf[0]*100))/100
            #print(conf)


            cls = int(box.cls[0])
            currClass = classNames[cls]
            if currClass == 'person' and conf > 0.3:
                dets.append([x1,y1,x2,y2,conf])

                cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
                cvzone.cornerRect(img, (x1, y1, w, h))

                # To blurr the BoundingBox
                roi = img[y1:y2, x1:x2]
                blurred_roi = cv2.GaussianBlur(roi, (15, 15), 0)
                img[y1:y2, x1:x2] = blurred_roi
                #print("Number of people : ",str(len(label)))




        trackers = tracker.update(np.array(dets))
        num_people = len(set(trackers[:, 4]))
        print("Number of People : ", num_people)

        # Make Sound if Number of people exceeds threshold
        threshold = 50

        if num_people > threshold:
            print("Threshold Exceeded !")
            playsound('Sound2.mp3')

        cv2.imshow("Image", img)
        cv2.waitKey(1)

