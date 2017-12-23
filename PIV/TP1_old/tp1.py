import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

global valor
valor = 0

moedas = {'0.01':0.01, '0.02':0.02, '0.05':0.05,
        '0.10':0.10, '0.20':0.20, '0.50':0.50, '1.00':1.00}

def improveImage(image):
    return cv2.bilateralFilter(image,22,30,30)

def imageBinary(image):
    return cv2.threshold(image,0,255,cv2.THRESH_OTSU)

def smoothImage(image):
    #TRATAMENTO DA IMAGEM
    #structuring element - uma imagem binaria
    matriz = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    #dilate melhor que o erode, imagens das moedas ficam mais redondas
    erode = cv2.erode(image,matriz,iterations=3)
    return erode

def centroides(image,img):
    #apanhar os contornos de uma imagem binaria
    cenas,contornos,hierarquia = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    array =[]
    for x in range(len(hierarquia[0])):
        if((hierarquia[0][x][2]!=-1) or((hierarquia[0][x][3]!=-1))):
            array.append(x)
    array.sort(reverse=True)
    for i in array:
        contornos.pop(i)

    centroide = []
    cx = []
    cy = []
    counter = 0
    for conta in contornos:
            momentos = cv2.moments(conta)
            #m00 equivale a area = cv2.contourArea(conta)
            if momentos['m00']!=0:
                cx.append(int(momentos['m10']/momentos['m00']))
                cy.append(int(momentos['m01']/momentos['m00']))
            centroide.append(conta)

    test = cv2.drawContours(img,centroide,-1,(255,255,0),thickness=2)
    cv2.imshow("contornos",test)
    return centroide,cx,cy


def distToCenter(centroide,cx,cy):
    corrected = []
    #maxima diferenca do raio calculado inicialmente e os pontos
    #provenientes dos contornos
    mx = 10
    counter =0
    #distance to center
    for x,y in zip(cx,cy):
        distref = np.sqrt(cv2.contourArea(centroide[counter])/np.pi)
        distref = distref+mx
        distref2 = distref-(2*mx)
        current = centroide[counter]
        filtered = filter(lambda f: True if (np.sqrt((f[0][0]-x)**2 + (f[0][1]-x)**2)>distref
        or np.sqrt((f[0][0]-x)**2 + (f[0][1]-x)**2)<distref2) else False, current)
        corrected.append(np.asarray(filtered))
        counter+=1

    #filtrar arrays que estejam a 0
    corrected = filter(lambda a: len(a)!=0 ,corrected)
    corrected = np.asarray(corrected)

    return corrected

def classifica(array):
    global valor
    for a in array:
        area = cv2.contourArea(a)
        if(area>= 0 and area<=10000):
            valor += moedas.get('0.01')
            print "Classifiquei: 1cent"
            print "area correspondente: " + str(area)

        if(area>= 11000 and area<11900):
            valor += moedas.get('0.02')
            print "Classifiquei: 2cent"
            print "area correspondente: " + str(area)

        if(area>= 11900 and area<14000):
            valor += moedas.get('0.10')
            print "Classifiquei: 10cent"
            print "area correspondente: " + str(area)

        if(area>= 14000 and area<15000):
            valor += moedas.get('0.05')
            print "Classifiquei: 5cent"
            print "area correspondente: " + str(area)

        if(area>= 15000 and area<17000):
            valor += moedas.get('0.20')
            print "Classifiquei: 20cent"
            print "area correspondente: " + str(area)

        if(area>= 17000 and area<19000):
            valor += moedas.get('1.00')
            print "Classifiquei: 1euro"
            print  "area correspondente: " + str(area)

        if(area>= 19000 and area<23000):
            valor += moedas.get('0.50')
            print "Classifiquei: 50cent"
            print "area correspondente: " + str(area)



def teste():

    # imagem ='P1.jpg' #WORKS
    # imagem ='P2.jpg' #WORKS
    # imagem ='P3.jpg' #WORKS less one coin
    imagem ='P4.jpg' #WORKS
    # imagem ='P5.jpg' #WORKS
    # imagem ='P6.jpg' #WORKS
    # imagem ='P7.jpg'
    # imagem ='P8.jpg'
    # imagem ='P9.jpg'

    #leitura da imagem em tons de cinzento
    img = cv2.imread(imagem,cv2.IMREAD_COLOR)
    ib,ig,ir = cv2.split(img)

    # color = ('b','g','r')
    # for i,col in enumerate(color):
    #     histr = cv2.calcHist([img],[i],None,[256],[0,256])
    #     plt.plot(histr,color = col)
    #     plt.xlim([0,256])
    # plt.show()
    # cv2.imshow('Imagem Original',img)
    #smoothing a imagem - MELHORAMNETO
    melhorada = improveImage(ir)
    # cv2.imshow('Imagem Melhorada',melhorada)
    #THRESH_TRIANGLE fica mais nitida - BINARIZACAO
    rt,thresh = imageBinary(melhorada)
    cv2.imshow('Imagem Binarizada',thresh)
    #erosao
    erode = smoothImage(thresh)
    # cv2.imshow('Imagem Erodida',erode)
    #centroides
    centroide,cx,cy = centroides(erode,img)
    #filtrar pontos que nao estao de acordo com o raio esperado
    array_final = distToCenter(centroide,cx,cy)

    classifica(array_final)
    cv2.waitKey(0)

    print "Valor final: " + str(valor)

if __name__ == "__main__":
    teste()
