import bwLabel
import psColor
import cv2
import numpy as np
#from numpy.core import multiarray

#circle = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#teste = cv2.imread('P1000698s.jpg')
#newimage1 = cv2.cvtColor(teste,cv2.COLOR_RGB2GRAY)
#newimage = cv2.threshold(newimage1,160,255,cv2.THRESH_BINARY)[1]
#graylevel, outimage = bwLabel.labeling(newimage)
#cv2.drawContours()
#cv2.imshow('outimage',outimage)
#cv2.imshow('image',newimage)
#cv2.waitKey()
#print "done"

#1.Reads Image
#objectImage = cv2.imread('P1000697s.jpg') #so moedas
#objectImage = cv2.imread('P1000698s.jpg') #so moedas
#objectImage = cv2.imread('P1000699s.jpg') #so moedas
objectImage = cv2.imread('P1000703s.jpg') #moedas + 1 objecto
#objectImage = cv2.imread('P1000705s.jpg') #so moedas (2juntas)
#objectImage = cv2.imread('P1000706s.jpg') #so moedas (2juntas)
#objectImage = cv2.imread('P1000709s.jpg') #moedas + 2 objectos
#objectImage = cv2.imread('P1000710s.jpg') #moedas + 3 objectos
#objectImage = cv2.imread('P1000713s.jpg') #moedas (2juntas) + objecto


#2.Converts to Gray level
#cvtcolorImage = cv2.cvtColor(objectImage,cv2.cv.CV_RGB2GRAY)

#3.Thresholds
imgSplit = cv2.split(objectImage)
flag,b = cv2.threshold(imgSplit[2],0,255,cv2.THRESH_OTSU) 
#4.Erodes the Thresholded Image
element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
b = cv2.erode(b, element)
contours, hierarchy = cv2.findContours(b,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    if cv2.contourArea(contours[i]) > 100.0 and cv2.contourArea(contours[i]) < 20500: #if the area of the object is below 100 it doesnt draw the contour
        if hierarchy[0][i][3] == -1:        
            (x,y),radius = cv2.minEnclosingCircle(contours[i])
            center = (int(x),int(y))
            radius = int(radius)
            cv2.circle(objectImage,center,radius,(0,0,255),3)
            print cv2.contourArea(contours[i])

cv2.imshow('cont_2',objectImage)
cv2.imshow('Eroded',b)
#cv2.imshow('original', objectImage)
#cv2.imshow('0',cv2.split(objectImage)[0])
#cv2.imshow('1',cv2.split(objectImage)[1])
#cv2.imshow('2',cv2.split(objectImage)[2])
cv2.waitKey()
print "done"
