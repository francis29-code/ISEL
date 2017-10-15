import cv2
import numpy as np
#leitura de uma imagem
img = cv2.imread("imageDB/falcon.jpg",cv2.IMREAD_COLOR)
# cv2.imshow('LEL',img)

#resize image
res75 = cv2.resize(img,None,fx=0.75,fy=0.75,interpolation = cv2.INTER_CUBIC)
# cv2.imshow('resized 75',res75)
# cv2.waitKey(0)
#espera da janela

background = cv2.imread("imageDB/florest.jpg",cv2.IMREAD_COLOR)
mask = cv2.imread("imageDB/mask.png",cv2.IMREAD_COLOR)
imgOut = cv2.add(cv2.multiply(img,mask,scale=1.0/255.),cv2.multiply(background,np.invert(mask),scale=1.0/255.))
cv2.imshow('croma',imgOut)
# cv2.waitKey(0)

#metodos de filtragem
imgBlur = cv2.blur(img,(4,4))
# cv2.imshow("imagem blured",imgBlur)

imgBlurMedian = cv2.medianBlur(img,5)
# cv2.imshow("imagem median blured", imgBlurMedian)
cv2.waitKey(0)
