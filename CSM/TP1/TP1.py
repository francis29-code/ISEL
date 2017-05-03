import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import sys
import os
path = str(sys.path[0])+"\\"

def saveImage(nome,image,quality=100,formato=".jpg"):
    newQ = (cv.IMWRITE_JPEG_QUALITY,quality)
    newName = path+nome+" - "+str(quality)+formato
    cv.imwrite(newName,image,newQ)
    print("\nsaveImage -> Qualidade: {} | Nome: {}".format(quality,newName[len(path):]))

def readImage(nome,caminho=path):
    img = cv.imread(caminho+nome)
    return img

def showImage(titulo,img):
    cv.imshow("Titulo: {}".format(titulo),img)

def imageSNR(original,amplificada):
    imageO = original.ravel()
    noise = original.astype(float) - amplificada.astype(float)
    imageA = noise.ravel()

    pOriginal = np.sum(imageO**2.)
    pAmplificada = np.sum(imageA**2.)
    SNR = 10*np.log10(pOriginal/pAmplificada)

    return SNR

def MSE(original,amplificada):
    linhas = len(original)
    colunas = len(original[0])
    noise = original.astype(float) - amplificada.astype(float)
    noiseR = noise.ravel()
    pAmplificada = np.sum(noiseR**2.)
    MSE = (1./(linhas*colunas))*pAmplificada

    return MSE

def PSNR(MSE):
    PSNR = 20*np.log10(255) - 10*np.log10(MSE)
    return PSNR

def compressionRatio(original,amplificada):
    sizeO = os.path.getsize(path+original)
    sizeA = os.path.getsize(path+amplificada)

    ratio = sizeO/sizeA

    return int(ratio)


def ex1():
    img = readImage('lenac.tif')
    showImage('Original Image', img)
    #indica-nos o datatype
    print ("Datatype: {}".format(img.dtype))
    #indica-nos o code ex UTF8
    print ("Shape: {}".format(img.shape))
    print ("Shape rows: {} | columns: {}".format(img.shape[0],img.shape[1]))
    cv.waitKey(0)
    cv.destroyAllWindows()

def ex2():
    #leitura da imagem incial
    img = readImage('lenac.tif')
    #gravação das duas imagens com diferentes percentagens de qualidade
    saveImage('imagem',img,80)
    saveImage('imagem',img,10)
    #leitura das imagens gravadas
    img80 = readImage('imagem - 80.jpg')
    img10 = readImage('imagem - 10.jpg')
    ## visualização das duas imagens gravadas
    showImage('Imagem 80', img80)
    showImage('Imagem 10', img10)

    #um pequeno "waiting" para a visualização das imagens
    cv.waitKey(0)

    #taxa de compressão é a divisão entre a original e a comprimida
    ratio10 = compressionRatio('lenac.tif','imagem - 10.jpg')
    print("\nRatio da imagem 10: {}%".format(ratio10))
    ratio80 = compressionRatio('lenac.tif','imagem - 80.jpg')
    print("Ratio da imagem 80: {}%".format(ratio80))

    #calculo da SNR
    SNR10  = imageSNR(img,img10)
    print("\nSNR dB - img10 -> {}dB".format(SNR10))
    SNR80 = imageSNR(img,img80)
    print("SNR dB img80 -> {}dB".format(SNR80))

    #calculo MSE
    MSE10 = MSE(img,img10)
    print("\nMSE - img10 -> {}".format(MSE10))
    MSE80 = MSE(img,img80)
    print("MSE - img80 -> {}".format(MSE80))

    #calculo PSNR
    PSNR10 = PSNR(MSE10)
    print("\nPSNR - img10 -> {}dB".format(PSNR10))
    PSNR80 = PSNR(MSE80)
    print("PSNR - img80 -> {}dB".format(PSNR80))


def ex3():
    # Y = R299=1000+G587=1000+B114=1000
    #leitura da imagem
    img = readImage('lenac.tif')
    #transformação da imagem para escala de cinzento
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #visualização da imagem
    showImage('Escala Cinzentos', imgGray)
    #guardar imagem
    saveImage('escalaCinzentos',imgGray,100,'.bmp')

    cv.waitKey(0)
    cv.destroyAllWindows()

def ex4():
    #leitura da imagem
    img = readImage("escalaCinzentos - 100.bmp")
    #histograma da imagem em Cinzentos
    plt.hist(img.ravel(),256,[0,256], color='r')
    plt.savefig(path+'histograma.png')
    plt.show()

    #cria array de valores UNICOS do histograma
    arrayUnique = np.unique(img)
    print("Niveis Cinzentos: {} ".format(len(arrayUnique)))

def ex5():
    #leitura imagem
    img = readImage('escalaCinzentos - 100.bmp')

    for i in range(8):
        imageBit = img & (2**i)
        showImage('BW - bit: {}'.format(i),imageBit*1.)
        saveImage('BW-bit'+str(i),imageBit,formato=".bmp")

    cv.waitKey(0)
    cv.destroyAllWindows()

def ex6():

    img = readImage('escalaCinzentos - 100.bmp')
    imageBit = img & 240
    showImage('BW - 4 bits',imageBit*1)
    saveImage('4bitsSignificativos',imageBit,formato=".bmp")
    cv.waitKey(0)
    cv.destroyAllWindows()


def ex7(angle):
    #width & height
    w ,h = (200,200)
    #criação do array da imagem
    img = np.ones((w,h,3),np.uint8)

    #uso da , indica que estamos a selecionar uma lista na posicação do slice
    # img[:,0:,int(w/2)] = (255,0,0)
    print("Valores Linhas: {} | Colunas: {}".format(img.shape[0],img.shape[1]))

    #fundo branco
    img[::] = (255,255,255)

    #centro da imagem
    center = (int(w/2),int(h/2))

    #limit
    times = int(360/angle)

    #angulo dado pelo utilizador
    for i in range(times):
        endingPX = int(center[0] + w * np.cos((i*angle) * np.pi / 180.0))
        endingPY = int(center[1] + w * np.sin((i*angle) * np.pi / 180.0))
        endingP = (endingPX,endingPY)

        cv.line(img,center,endingP,(0,0,0))

    showImage('Imagem Criada',img)
    saveImage('ImagemCriada',img,formato=".jpg")

    cv.waitKey(0)
    cv.destroyAllWindows()

    print("ex7")



if __name__ == "__main__":
    # ex1()
    # ex2()
    # ex3()
    ex4()
    # ex5()
    # ex6()
    # ex7(2)
