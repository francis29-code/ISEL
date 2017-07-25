# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:45:06 2017

@author: joao_
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import math

def bitsSignificativos(img):
    x = 0
    for i in range(0,255):
        if(i == 2**x):
            y = img & 2**x
            cv2.imshow('Nbits: ' + str(i), y * 1.0)
            cv2.imwrite('images/lena_' + str(i) + '.bmp', y)
            x = x + 1
            
def taxaCompressao(original,comprimido):
    txComp = float(original) / float(comprimido)
    return round(txComp,2)
    
def SNR(original,comprimido):
    oReshape = original.ravel()
    pSinal = np.sum(oReshape**2.)
    
    ruido = original.astype(float)-comprimido.astype(float)
    rReshape = ruido.ravel()
    pRuido = sum(rReshape**2.)
    
    snr = 10*math.log10(pSinal/pRuido)
    return round(snr,2)
    
def MSE(original, comprimido):
	
     err = np.sum((original.astype("float") - comprimido.astype("float")) ** 2)
     err /= float(original.shape[0] * original.shape[1])
     print err
     return round(err,2)

def PSNR(original,comprimido):
    mse = MSE(original,comprimido)
    MAX = np.amax(original)
    psnr = 20*math.log10(MAX) - 10*math.log10(mse)
    return round(psnr,2)
    
if __name__ == "__main__":
    
    # EX1
    lena = cv2.imread("images/lenac.tif")
    #cv2.imshow("Lena original", lena)
#    print "dtype: ", lena.dtype
#    print "shape: ", lena.shape
    
    #EX2
    cv2.imwrite('images/lena80.jpg', lena, (cv2.IMWRITE_JPEG_QUALITY,80))
    cv2.imwrite('images/lena10.jpg', lena, (cv2.IMWRITE_JPEG_QUALITY,10))
    lenajpg = cv2.imread("images/lenacc.jpg")
    lena80 = cv2.imread("images/lena80.jpg")
    lena10 = cv2.imread("images/lena10.jpg")
    lenaSize = os.path.getsize("images/lenac.tif")
    lenaSizejpg = os.path.getsize("images/lenacc.jpg")
    lena10Size = os.path.getsize("images/lena10.jpg") 
    lena80Size = os.path.getsize("images/lena80.jpg")
#    print lenaSize, lenaSizejpg, lena80Size, lena10Size
    txC80, txC10 = taxaCompressao(lenaSizejpg, lena80Size) , taxaCompressao(lenaSizejpg, lena10Size)
    SNR80, SNR10 = SNR(lenajpg, lena80), SNR(lenajpg, lena10)
    psnr80, psnr10 = PSNR(lenajpg,lena80), PSNR(lenajpg, lena10)
#    print "Tamanho imagem original: " , os.path.getsize("images/lenac.tif")
#    print "Tamanho imagem original jpg: " , os.path.getsize("images/lenacc.jpg")
#    print "Tamanho imagem com 80% qualidade: " , os.path.getsize("images/lena80.jpg")
#    print "Tamanho imagem com 10% qualidade: " , os.path.getsize("images/lena10.jpg")
#    print "Taxa de Compressão 80%: ", txC80
#    print "Taxa de Compressão 10%: ", txC10
#    print "SNR 80%: ",  SNR80
#    print "SNR 10%: ",  SNR10
#    print "PSNR 80%: ", psnr80
#    print "PSNR 10%: ", psnr10
    
    #EX3
    lenaG = cv2.cvtColor(lena , cv2.COLOR_BGR2GRAY)
    #cv2.imshow('Imagem em tons de cinzento', lenaG)
    #cv2.imwrite('images/lenaCinzento.jpg',lenaG)
    print "Tamanho da imagem original: ", lenaSize, lenaSizejpg
    print "Tamanho da imagem cinzenta: ", os.path.getsize("images/lenaCinzento.jpg") 
    
    #EX4
#    plt.hist(lenaG.ravel(),256,[0,256], facecolor = 'red')
#    plt.xlabel('Niveis de cinzento')
#    plt.ylabel('Numero de ocorrencias')
#    plt.title('Histograma da imagem em tons de cinzento')
#    plt.grid(True)
#    plt.savefig('images/histograma.jpg')
#    plt.show()
#    print np.unique(lenaG).size
    
    #EX5
#    bitsSignificativos(lenaG)
    
    #EX6
#    fourSignificantBits = lenaG & 240
#    cv2.imshow('Quatro bits mais significativos', fourSignificantBits )
#    cv2.imwrite('images/quatrobits.jpg', fourSignificantBits)
    
    #EX7
    x, y = 400, 400
    newImg = np.zeros([x,y,3], dtype=np.uint8)
    newImg.fill(255)
    
    for i in range(newImg.size):
        if(i >= (newImg.size / 2) - 1):
            newImg[i] = 0
            
#    cv2.imshow('new image', newImg)    
    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()