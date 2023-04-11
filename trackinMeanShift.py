import cv2
roi=cv2.imread('roi.jpg')
roiHsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
roiHist=cv2.calcHist([roiHsv],[0],None,[180],[0,180])
roiNorm=cv2.normalize(roiHist,roiHist,0,255,cv2.NORM_MINMAX)

term_criteria=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,1)

video=cv2.VideoCapture(0)
while video.isOpened():
    ret,frame=video.read()
    #cv2.imshow('asbhjka',frame)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask=cv2.calcBackProject([hsv],[0],roiNorm,[0,180],1)
    
    _,meanshift=cv2.meanShift(mask,(215,175,210,130),term_criteria)
    x,y,w,h=meanshift
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow('frame',frame)
    key=cv2.waitKey(20)
    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows()