import cv2;
import numpy as np;
upper_body_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
f1 = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml');
cap=cv2.VideoCapture(0);
# prevframe = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]];
prevhead = 320;
timer = 0;
counter = 0;
while True:
    ret, frame=cap.read();
    grayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
    # retraval , threshold = cv2.threshold(grayframe,155,255,cv2.THRESH_BINARY);
    upperbody = upper_body_cascade.detectMultiScale(grayframe, 1.3, 5);
    # for i in range(0,641):
    #     for j in range(0,481):
    #         if(frame[j][i] - prevframe[j][i]<20):
    #             count += 1;
    
    for (x,y,w,h) in upperbody:
        if(len(upperbody)==1):    
            cv2.rectangle(grayframe,(x,y),(x+w,y+h),(255,0,0),2); 
        counter += abs((x-prevhead));
        prevhead = x;
    timer += 1;  
    # print(grayframe[2][25]-prevframe[2][25])
    # print(np.shape(grayframe));
    cv2.imshow('frame',grayframe);
    # prevframe = grayframe;
    if(timer == 300):
        if(counter > 1000 ):
            print('times up  user not focuesed');
        else:
            print('user focuesed');
        timer = 0 ;
        counter = 0;                  
    k=cv2.waitKey(5) & 0xFF
    if k==27:                                                        
        break;
cap.release()
cv2.destroyAllWindows()    