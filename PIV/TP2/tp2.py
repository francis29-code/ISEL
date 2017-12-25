import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
current_time = 0
last_time = 0
last_area = 0
while( cap.isOpened() ) :
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh1 = cv2.threshold(blur,100,255,cv2.THRESH_BINARY +cv2.THRESH_OTSU)
    cv2.imshow('binarizada', thresh1)

    nonsense, contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #
    max_area=0

    for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i
    cnt=contours[ci]
    print "current_time : ", current_time
    print "last_time : ", last_time
    if current_time - last_time > 60:
        last_time += 60
        last_area = max_area
    print "last_area",last_area
    print "max_area",max_area
    current_time += 1

    print cnt

    hull = cv2.convexHull(cnt)
    moments = cv2.moments(cnt)
    if moments['m00']!=0:
                cx = int(moments['m10']/moments['m00']) # cx = M10/M00
                cy = int(moments['m01']/moments['m00']) # cy = M01/M00

    centr=(cx,cy)
    cv2.circle(img,centr,5,[0,0,255],2)
    cv2.drawContours(img,[cnt],0,(0,255,0),2)
    cv2.drawContours(img,[hull],0,(255,0,0),2)

    # cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    # hull = cv2.convexHull(cnt,returnPoints = False,clockwise=True)

    # if(1):
    #            defects = cv2.convexityDefects(cnt,hull)
    #            print "defects {}",defects[0]
    #            print "hull {}",hull
    #            mind=0
    #            maxd=0
    #            print defects.shape[0]
    #            if(defects is None):continue
    #            start = tuple(cnt[hull[0][0]][0])
    #            end = tuple(cnt[hull[1][0]][0])
    #            far = tuple(cnt[hull[2][0]][0])
    #            cv2.line(img,start,end,[0,255,0],2)
    #            cv2.circle(img,far,5,[0,0,255],-1)

            #    for i in range(defects.shape[0]):
            #         print "defects in for : ",defects[i,0]
            #         s,e,f,d = defects[i,0]
            #         print "s {}",s
            #         print "e {}",e
            #         print "f {}",f
            #         start = tuple(cnt[s][0])
            #         end = tuple(cnt[e][0])
            #         far = tuple(cnt[f][0])
            #         cv2.line(img,start,end,[0,255,0],2)

            #         cv2.circle(img,far,5,[0,0,255],-1)
            # #    print(i)
            #    i=0
    cv2.imshow('input',img)

    k = cv2.waitKey(10)
    if k == 27:
        break
