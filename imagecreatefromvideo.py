import cv2
video=cv2.VideoCapture(0)
while video.isOpened():
    _,firstFrame=video.read()
    cv2.rectangle(firstFrame,(210,170),(430,310),(0,255,0),2)
    cv2.line(firstFrame,(210,170),(230,170),(0,0,255),5)
    cv2.line(firstFrame,(210,170),(210,190),(0,0,255),5)

    cv2.line(firstFrame,(430,170),(410,170),(0,0,255),5)
    cv2.line(firstFrame,(430,170),(430,190),(0,0,255),5)

    cv2.line(firstFrame,(210,310),(210,290),(0,0,255),5)
    cv2.line(firstFrame,(210,310),(230,310),(0,0,255),5)

    cv2.line(firstFrame,(430,310),(410,310),(0,0,255),5)
    cv2.line(firstFrame,(430,310),(430,290),(0,0,255),5)
    cv2.imshow('first',firstFrame)
    key=cv2.waitKey(10)
    if key==ord('q'):
        break
    elif key==ord('w'):
        roi=firstFrame[175:305,215:425]
        cv2.imshow('roi',roi)
        cv2.imwrite('roi.jpg',roi)
        cv2.waitKey(0)
cv2.destroyAllWindows()