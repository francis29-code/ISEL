# filename: bwLabel Module
import cv2
import numpy as np

def labeling(bwImage):
    bw = bwImage.copy()
    (contourSeq, [contourHierarchy]) = cv2.findContours(bw, \
                    cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    contours =[]
    grayLevel = 0
    outImage = np.zeros(bwImage.shape)
    for i in range(len(contourSeq)):
        cX = contourSeq[i]
        # tests if it is not an internal contour and its area is grater than a minArea value
        if cv2.contourArea(cX) > 1000.0 and contourHierarchy[i][3] < 0 and (contourHierarchy[i][2]< 0 and not eqcent(contourSeq[i],contourHierarchy[i][2])):
            approx = cv2.approxPolyDP(cX,0.04*cv2.arcLength(cX,True),True)
            if len(approx) >= 6:
                grayLevel = grayLevel+1;
                color = (grayLevel,grayLevel,grayLevel)
                cv2.drawContours(outImage, contourSeq, i, color, 1)
                contours.append(cX)      
        
    return contours, grayLevel, outImage

def eqcent(cont1,cont2):
    m1 = cv2.moments(cont1)
    m2 = cv2.moments(cont2)
    c1x = int(m1['m10']/m1['m00'])
    c1y = int(m1['m01']/m1['m00'])
    c2x = int(m2['m10']/m2['m00'])
    c2y = int(m2['m01']/m2['m00'])
    return (c1x,c1y) == (c2x,c2y)
