from sre_constants import SUCCESS
from turtle import filling
import cv2 
import mediapipe as mp
import time
import os
import handtracking_module as htm
#
wCam , hCam = 900 , 480 
#
folderPath = "/Users/nisargwath/Desktop/code/openCV/opencv/advance Opencv/handtracking/fin"
myList = os.listdir(folderPath)
print(myList)
overlayList  = []
for imPath in myList:
    image = cv2.imread(f"{folderPath}/{imPath}")
    # print(f"{folderPath}/{imPath}")
    overlayList.append(image)
print(len(overlayList))

myList = os.listdir()

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.HandDetector()

tipIds = [4, 8, 12, 16, 20]

while True:
    success , img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)
    
    if len(lmList) != 0:
        fingers = []
        if lmList[tipIds[0]][1] > lmList[tipIds[0]- 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1,5):
            #thumb
            
            #finger    
            if lmList[tipIds[id]][2] < lmList[tipIds[id]- 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
                
        # print(fingers)  
        totalFingers = fingers.count(1)
        print(totalFingers)
        h , w,c = overlayList[totalFingers -1].shape
        img[0:h, 0:w] = overlayList[totalFingers -1]
        
        # cv2.rectangle(img, (20,200), (170, 700), (0,255,0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (200,700), cv2.FONT_HERSHEY_PLAIN, 8, (250, 0 ,0),18)

        
            
    cTime = time.time( )
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS: {int(fps)}", (400,700), cv2.FONT_HERSHEY_PLAIN, 3, (250, 0 ,0),3)
    

    cv2.imshow("Result", img)
    cv2.waitKey(1)