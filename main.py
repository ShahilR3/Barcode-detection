import cv2
import numpy as np
from pyzbar.pyzbar import decode
from playsound import playsound

def Cartoon(image_color):
    output_image = cv2.stylization(image_color, sigma_s = 100, sigma_ = 0.3)
    return output_image
def LiveCamEdgeDetection_canny(image_color):
    threshold_1 = 30
    threshold_2 = 80
    image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(image_gray, threshold_1,threshold_2)
    return canny

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()

while cap.isOpened():
    success,frame = cap.read()
    frame = cv2.flip(frame,1)

    detectedBarcode = decode(frame)
    if  detectedBarcode:
        for barcode in detectedBarcode:
            myData = barcode.data.decode('utf-8')
            print(myData)

            if myData in myDataList:
                myOutput = 'Authorized'
                myColor = (0, 0, 0)
                playsound("C:\\Users\\shahi\\Downloads\\beep-01.mp3")

            else:
                myOutput = 'Un-Authorized'
                myColor = (0, 0, 0)
                playsound("C:\\Users\\shahi\\Downloads\\Censor BEEP Sound Effect-TV Error Clip.mp3")


            if barcode.data != "":
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(frame, [pts], True, myColor, 5)
                pts2 = barcode.rect
                cv2.putText(frame, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)
                print(barcode.data)
                break

    cv2.imshow('scanner' , LiveCamEdgeDetection_canny(frame))
    if cv2.waitKey(1) == ord('q'):
        break