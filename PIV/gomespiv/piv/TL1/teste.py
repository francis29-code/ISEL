# -*- coding: utf-8 -*-
import bwLabel
import psColor
import cv2
import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX
objectImage = cv2.imread('P1000697s.jpg') #8 moedas
#objectImage = cv2.imread('P1000698s.jpg') #5 moedas
#objectImage = cv2.imread('P1000699s.jpg') #5 moedas
#objectImage = cv2.imread('P1000703s.jpg') #4 moedas + 1 objecto
#objectImage = cv2.imread('P1000705s.jpg') #4 moedas (2juntas)
#objectImage = cv2.imread('P1000706s.jpg') #5 moedas (2juntas)
#objectImage = cv2.imread('P1000709s.jpg') #3 moedas + 2 objectos + meia moeda 
#objectImage = cv2.imread('P1000710s.jpg') #3 moedas + 3 objectos 
#objectImage = cv2.imread('P1000713s.jpg') #3 moedas (2juntas) + 1 objecto
maxIntensity = 255.

newimage = maxIntensity*(objectImage/maxIntensity)**0.01
newimage = np.array(newimage, dtype='uint8')

imgSplit = cv2.split(newimage)
flag,b = cv2.threshold(imgSplit[2],0,255,cv2.THRESH_OTSU) 

element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(14,14))
b = cv2.erode(b, element)
contours, graylevel, outimage = bwLabel.labeling(b)
#outimage = cv2.dilate(outimage,element)
colormap = psColor.CreateColorMap(graylevel+1)
pseudocolor = psColor.Gray2PseudoColor(outimage, colormap)
element2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
pseudocolor = cv2.dilate(pseudocolor,element2)
values ={'1 cent':[7900,9100,1],'2 cent':[10900,12100,2],'5 cent':[13900,15100,5],'10 cent':[12100,13100,10],'20 cent':[15900,17100,20],
    '50 cent':[19000,21100,50], '1 eur':[17100,19100,100]}
total = 0
for i in contours:
    (x,y),radius = cv2.minEnclosingCircle(i)
    area = cv2.contourArea(i)
    valor = str(area)
#    if area >= 7900 and area <9100:
#        valor = '1 cent'
#    if area >= 10900 and area < 12100:
#        valor = '2 cent'
#    if area >= 13900 and area < 15100:
#        valor = '5 cent'
#    if area >= 12100 and area < 13100:
#        valor = '10 cent'
#    if area >= 15900 and area < 17100:
#        valor = '20 cent'
#    if area >= 19000 and area < 21100:
#        valor = '50 cent'
#    if area >= 17100 and area < 19100:
#        valor = '1 eur'
#    if valor == 'desconhecido':
#        valor = str(area)
            
#    for key,value in values.iteritems():
#        if value[0] <= area < value[1]:
#            valor = key
#            total+= value[2]
#            break
    cv2.putText(pseudocolor,valor,(int(x)-30,int(y)),font,0.7,(255,255,255),2,5)

cv2.putText(pseudocolor,str(total),(5,150),font,3,(255,255,255),2,5)
#cv2.imshow('original',newimage )
#cv2.imshow('before label', b)
#cv2.imshow('after label', pseudocolor)
teste = cv2.add(objectImage,pseudocolor)
cv2.imshow('teste',teste)
#cv2.imshow('derp',newimage)
cv2.waitKey()