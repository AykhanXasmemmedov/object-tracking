import numpy as np
import cv2
#we create histogram of image which we want to find from video
roi=cv2.imread('roi.jpg')
roihsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
roiHist=cv2.calcHist([roihsv],[0],None,[180],[0,180])
roiNorm=cv2.normalize(roiHist,roiHist,0,255,cv2.NORM_MINMAX)

criteria=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,1)

video=cv2.VideoCapture(0)
while video.isOpened():
    ret,frame=video.read()
    if ret==True:
        frameHsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask=cv2.calcBackProject([frameHsv],[0],roiNorm,[0,180],1)

        ret,track_window=cv2.CamShift(mask,(215,175,210,130),criteria)

        points=cv2.boxPoints(ret)
        points=np.int0(points)
        cv2.polylines(frame,[points],True,(0,255,0),2)
        cv2.imshow('mask',frame)

        key=cv2.waitKey(20)
        if key==ord('q'):
            break    
    else:
        print('error: video can not read')

video.release()
cv2.destroyAllWindows()



