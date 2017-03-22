import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import sys
path = str(sys.path[0])+"\\"

def saveImage(nome,image,quality=100,formato=".jpg"):
    newQ = (cv.IMWRITE_JPEG_QUALITY,quality)
    newName = path+nome+" - "+str(quality)+formato
    cv.imwrite(newName,image,newQ)
    print("\nsaveImage -> Qualidade: {} | Nome: {}".format(quality,newName[len(path):]))

def readImage(nome):
    img = cv.imread(path+nome)
    return img


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
    #gravação das duas imagens com diferentes percentagens de qualidade
    saveImage('imagem',img,80)
    saveImage('imagem',img,10)
    #leitura das imagens gravadas
    img80 = readImage('imagem - 80.jpg')
    img10 = readImage('imagem - 10.jpg')
    ## visualização das duas imagens gravadas
    cv.imshow('Imagem 80', img80)
    cv.imshow('Imagem 10', img10)
    #um pequeno "waiting" para a visualização das imagens
    cv.waitKey(0)

    #taxa de compressão é a divisão entre a original e a comprimida


    #calculo da SNR
    imgR = img.ravel()
    dif = img.astype(float)-img10.astype(float)
    difR = dif.ravel()
    pOriginal = np.sum(imgR**2.)
    pRuido = np.sum(difR**2.)
    SNR  = 10*np.log10(pOriginal/pRuido)
    print("\nSNR - dB - img10 -> {}".format(SNR))

    # SNR  = 10*np.log10()
    # print("\nSNR - dB -> {}".format(SNR))


    #calculo MSE
    MSE = 1/(len(img)*len(img[0])) * (np.sum(img-img10)**2)
    print("\nMSE -> {}".format(MSE))
    #calculo PSNR
    PSNR = 10*np.log10(255/MSE)
    print("\nPSNR -> {}".format(PSNR))


def ex3():
    # Y = R299=1000+G587=1000+B114=1000
    #leitura da imagem
    img = cv.imread(path+'lenac.tif')
    #transformação da imagem para escala de cinzento
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #visualização da imagem
    cv.imshow('Escala Cinzentos',imgGray)
    #guardar imagem
    saveImage('escalaCinzentos',imgGray,100,'.bmp')

    cv.waitKey(0)

def ex4():
    #leitura da imagem
    img = readImage("escalaCinzentos - 100.bmp")
    #histograma da imagem em Cinzentos
    plt.hist(img.ravel(),256,[0,256])
    plt.show()

    arrayUnique = np.unique(img)
    print("Niveis Cinzentos: {} ".format(len(arrayUnique)))


if __name__ == "__main__":
    # ex1()
    ex2()
    # ex3()
    # ex4()

    # b = np.array([[2,3,4,4],[2,3,4,5]])
    # print("length linhas: {} - length colunas: {}".format(len(b),len(b[0])))
