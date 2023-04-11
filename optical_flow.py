import cv2
import numpy as np

features=dict(winSize=(25,25),maxLevel=4,criteria=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,0.03))

def mouse(event,x,y,flags,params):
    global point,pointSelected,p0
    if event==cv2.EVENT_LBUTTONDOWN:
        point=(x,y)
        pointSelected=True
        p0=np.array([[x,y]],dtype='float32')
        
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouse)
point=()
pointSelected=False

video=cv2.VideoCapture(0)
ret,firstFrame=video.read()
grayfirstframe=cv2.cvtColor(firstFrame,cv2.COLOR_BGR2GRAY)

while video.isOpened():
    ret,frame=video.read()
    frame=cv2.flip(frame,1)
    grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if pointSelected==True:
        cv2.circle(frame,point,5,(255,0,0),2)
        newPoints,status,error=cv2.calcOpticalFlowPyrLK(grayfirstframe,grayframe,p0,None,**features)
        
        a,b=newPoints.ravel()
        cv2.circle(frame,(int(a),int(b)),5,(0,0,255),-1)

        #p0=newPoints
        grayfirstframe=grayframe.copy()


    cv2.imshow('frame',frame)
    key=cv2.waitKey(27)
    if key==ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()
p0
