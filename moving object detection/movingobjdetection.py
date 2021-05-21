import cv2
import time
import imutils

cam = cv2.VideoCapture(0)
time.sleep(1)

import cv2
import time
import imutils

cam = cv2.VideoCapture(0)
time.sleep(1)

firstFrame=None
area = 500
num=0
while True:
    _,img = cam.read()
    text = "Normal"
    img = imutils.resize(img, width=500)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)
    if firstFrame is None:
        firstFrame = grayImg
        continue
    imgDiff = cv2.absdiff(firstFrame, grayImg)
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
    threshImg = cv2.dilate(threshImg,None,iterations=2)
    cnts = cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
            if cv2.contourArea(c) < area:
                    continue
            (x, y, w, h) = cv2.boundingRect(c) 
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Moving Object detected"

    num=num+1
    num1=str(num)
    print(text)
    cv2.putText (img, text, (10, 20),
           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText (img, num1, (10, 50),
           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("VideoStream",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
print("Number of times moving object detected = "+ str(num))
