import numpy as np
import cv2 as cv
import sys
caminho = str(sys.path[0])+"\\"


def ex1():

    img = cv.imread(caminho+'lenac.tif')
    cv.imshow('Original Image', img)

    #indica-nos o datatype
    print (img.dtype)

    #indica-nos
    print (img.shape)

    cv.waitKey(0)
    cv.destroyAllWindows()

def ex2():
    #leitura da imagem incial
    img = cv.imread(caminho+'lenac.tif')

    #gravação das duas imagens
    cv.imwrite(caminho+'imagem80.jpg',img,(cv.IMWRITE_JPEG_QUALITY,80))
    cv.imwrite(caminho+'imagem10.jpg',img,(cv.IMWRITE_JPEG_QUALITY,10))

    #leitura das imagens gravadas
    img80 = cv.imread(caminho+'imagem80.jpg')
    img10 = cv.imread(caminho+'imagem10.jpg')

    ##duas imagens gravadas
    cv.imshow('Imagem 80', img80)
    cv.imshow('Imagem 10', img10)

    #necessário para visualização da imagem
    cv.waitKey(0)

    #calculo da SNR
    SNR  = 10*np.log10((np.sum(img10)**2)/np.sum((img10-img80))**2)

    print(str(SNR))





#
# px = img[100,100]
#
# print("BLUE GREEN RED")
# print(px)



if __name__ == "__main__":
    # ex1()
    ex2()
