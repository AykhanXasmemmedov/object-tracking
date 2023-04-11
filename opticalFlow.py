import cv2
import numpy as np
features=dict(maxCorners=200,qualityLevel=0.3,minDistance=7,blockSize=7)
lk_featrues=dict(winSize=(15,15),maxLevel=2,criteria=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,0.03))
color=np.random.randint(0,255,(100,3))

video=cv2.VideoCapture(0)

ret,firstFrame=video.read()
grayfirstFrame=cv2.cvtColor(firstFrame,cv2.COLOR_BGR2GRAY)

p0=cv2.goodFeaturesToTrack(grayfirstFrame,mask=None,**features)

mask=np.zeros_like(firstFrame)

while video.isOpened():
    ret,frame=video.read()
    frame=cv2.flip(frame,1)
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    newpoints,status,error=cv2.calcOpticalFlowPyrLK(grayfirstFrame,grayFrame,p0,None,**lk_featrues)
    newpoints=np.array(newpoints,dtype='float32')
    well_new_point=newpoints[status==1]
    well_old_point=p0[status==1]

    for i,(new,old) in enumerate(zip(well_new_point,well_old_point)):
        a,b=new.ravel()
        c,d=old.ravel()
        
        cv2.line(mask,(int(a),int(b)),(int(c),int(d)),color[i].tolist(),2)
        cv2.circle(frame,(int(a),int(b)),5,color[i].tolist(),-1)
    
    track_frame=cv2.add(frame,mask)
    cv2.imshow('track_frame',track_frame)

    key=cv2.waitKey(27)
    if key==ord('q'):
        break
    grayfirstFrame=grayFrame.copy()
    p0=well_new_point.reshape(-1,1,2)

video.release()
cv2.destroyAllWindows()

