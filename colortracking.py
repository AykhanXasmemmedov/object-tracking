import cv2
import numpy as np

video=cv2.VideoCapture(0)
lowerbound=np.array([100,100,100])
upperbound=np.array([130,255,255])
ret,firstframe=video.read()
Height,Width=firstframe.shape[:2]
points=[]
Mask=np.zeros_like(firstframe)
while video.isOpened():
    ret,frame=video.read()
    blur=cv2.GaussianBlur(frame,(5,5),0)
    if ret==True:
        hsvframe=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(hsvframe,lowerbound,upperbound)

        contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        if len(contours)>0:
            c=max(contours,key=cv2.contourArea)
            (x,y),radius=cv2.minEnclosingCircle(c)
            M=cv2.moments(c)
            try:
                center=(int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            except:
                center=(int(Height/2),int(Width/2))
            if radius>40:
                points.append(center)
                cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,0),3)
                cv2.circle(frame,center,5,(0,255,0),-1)
                try:
                    i= len(points)-1
                    cv2.line(Mask,points[i-1],points[i],(0,255,0),2)
                except:
                    pass
        frame=cv2.add(frame,Mask)
        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        key=cv2.waitKey(4)
        if key==ord('q'):
            break
    else:
        print('video can not read')
        break

video.release()
cv2.destroyAllWindows()