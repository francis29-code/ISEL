# -*- coding: utf-8 -*-
##TP1 PIV
import bwLabel
import psColor
import cv2
import numpy as np
import math


#image = 'P1000697s.jpg' #8 moedas
#image = 'P1000698s.jpg' #5 moedas
#image = 'P1000699s.jpg' #5 moedas
#image = 'P1000703s.jpg' #4 moedas + 1 objecto
image = 'P1000705s.jpg' #4 moedas (2juntas)
#image = 'P1000706s.jpg' #5 moedas (2juntas)
#image = 'P1000709s.jpg' #3 moedas + 2 objectos + meia moeda 
#image = 'P1000710s.jpg' #3 moedas + 3 objectos 
#image = 'P1000713s.jpg' #3 moedas (2juntas) + 1 objecto

def loadImage(filename):
    return cv2.imread(filename)
    
def brightEnhance(image):
    maxIntensity = 255.
    newimage = maxIntensity*(image/maxIntensity)**0.01
    newimage = np.array(newimage, dtype='uint8')
    return newimage

def processImage(image):
    imgSplit = cv2.split(image)
    flag,b = cv2.threshold(imgSplit[2],0,255,cv2.THRESH_OTSU) 

    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(14,14))
    b = cv2.erode(b, element)

    contours, graylevel, outimage = bwLabel.labeling(b)
    #outimage = cv2.dilate(outimage,element)
    colormap = psColor.CreateColorMap(graylevel+1)
    pseudocolor = psColor.Gray2PseudoColor(outimage, colormap)
   
    element2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
    pseudocolor = cv2.dilate(pseudocolor,element2)
    
    return pseudocolor,contours
    
def count(image, contours):
    font = cv2.FONT_HERSHEY_SIMPLEX
    total = 0
    values ={'1 cent':[7900,9100,1],'2 cent':[10900,12100,2],'5 cent':[13900,15100,5],'10 cent':[12100,13100,10],
    '20 cent':[15900,17100,20],'50 cent':[19000,21100,50], '1 eur':[17100,19100,100]}
    for i in contours:
        (x,y),radius = cv2.minEnclosingCircle(i)
        area = cv2.contourArea(i)
        valor = str(area)
        for key,value in values.iteritems():
            if value[0] <= area < value[1]:
                valor = key
                total+= value[2]
                break
        cv2.putText(image,valor,(int(x)-30,int(y)),font,0.7,(255,255,255),2,5)
    total = total/100.
    total = "%.02f" % total
    cv2.putText(image,str(total)+" euros",(5,60),font,2,(255,255,255),2,5)
    return image
    
def finalRender(originalImage,values):
    newimage = cv2.add(originalImage,values)
    return newimage
    
def MoneyCounter(filename):
    start = loadImage(filename)
    copy = start.copy()    
    copy = brightEnhance(copy)
    copy,contours = processImage(copy)
    copy = count(copy,contours)
    final = finalRender(start,copy)
    cv2.imshow('contador',final)
    cv2.waitKey()
    
MoneyCounter(image)
