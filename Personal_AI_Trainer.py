import cv2
import numpy as np
import time
import PoseEstimationMod as pem

cap = cv2.VideoCapture("TrainingVideos/BicepCurls1.mp4")
detector = pem.poseDetector()
count = 0
dir = 0
pTime = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img, draw=False)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # Right Arm
        # detector.findAngle(img, 12, 14, 16)
        # Left Arm
        angle = detector.findAngle(img, 11, 13, 15)
        per = np.interp(angle, (210, 330), (0, 100))
        bar = np.interp(angle, (220, 330), (650, 100))

        # Check for the Bicep Curls
        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0
        # Drawing Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), (255, 0, 255), 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, f"{int(per)}%", (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 255), 4)
        #Draw Curl Count
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 0), 25)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS:{int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
    cv2.imshow("Image", img)
    cv2.waitKey(1)