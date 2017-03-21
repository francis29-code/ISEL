import numpy as np
import cv2 as cv
import sys
path = str(sys.path[0])+"\\"

def saveImage(nome,image,quality=100):
    newQ = (cv.IMWRITE_JPEG_QUALITY,quality)
    newName = path+nome+" - "+str(quality)+'.jpg'
    cv.imwrite(newName,image,newQ)
    print("saveImage -> Qualidade: {} | Nome: {}".format(quality,newName[len(path):]))


def ex1():

    img = cv.imread(path+'lenac.tif')
    cv.imshow('Original Image', img)

    #indica-nos o datatype
    print (img.dtype)

    #indica-nos
    print (img.shape)

    cv.waitKey(0)
    cv.destroyAllWindows()

def ex2():
    #leitura da imagem incial
    img = cv.imread(path+'lenac.tif')

    #gravação das duas imagens
    saveImage('imagem',img,80)
    saveImage('imagem',img,10)

    #leitura das imagens gravadas
    img80 = cv.imread(path+'imagem - 80.jpg')
    img10 = cv.imread(path+'imagem - 10.jpg')

    ##duas imagens gravadas
    cv.imshow('Imagem 80', img80)
    cv.imshow('Imagem 10', img10)

    #necessário para visualização da imagem
    cv.waitKey(0)

    #calculo da SNR
    SNR  = 10*np.log10((np.sum(img10)**2)/(np.sum((img10-img80))**2))

    print("\nSNR - dB -> " + str(SNR))

    #calculo MSE
    # (1/lenLinhas * lenColunas) * [somatorioAP - somatorioOR]**2

    #calculo PSNR
    # 10log10(255**2/MSE)

def ex3():







#
# px = img[100,100]
#
# print("BLUE GREEN RED")
# print(px)



if __name__ == "__main__":
    # ex1()
    ex2()
