import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

intervalos = {0.01:[4999,6000], 0.02:[6000,9210], 0.10:[9210,10650],
        0.05:[10650,11550], 0.20:[11550,13500], 1.0:[13500,15000], 0.50:[15000,23000]}

def brightEnhance(image):
    maxIntensity = 255.
    newimage = maxIntensity*(image/maxIntensity)**0.01
    newimage = np.array(newimage, dtype='uint8')
    return newimage


def improveImage(image):
    return cv2.bilateralFilter(image,22,30,30)

def imageBinary(image):
    return cv2.threshold(image,0,255,cv2.THRESH_OTSU)

def smoothImage(image):
    #TRATAMENTO DA IMAGEM
    #structuring element - uma imagem binaria
    matriz = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(14,14))
    #dilate melhor que o erode, imagens das moedas ficam mais redondas
    erode = cv2.erode(image,matriz,iterations=5)

    matriz = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))

    dilate = cv2.dilate(erode,matriz,iterations=7)
    return dilate

def centroides(image,img):
    #apanhar os contornos de uma imagem binaria
    indiferente,contornos,hierarquia = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    counter = 0;
    for x in range(len(hierarquia[0])):
        if((hierarquia[0][x][2]!=-1) or((hierarquia[0][x][3]!=-1))):
            #retira contornos com contornos interiores
            contornos.pop(x+counter)
            counter+=1

    contours = []
    cx = []
    cy = []
    counter = 0
    for conta in contornos:
            momentos = cv2.moments(conta)
            #m00 equivale a area = cv2.contourArea(conta)
            if momentos['m00']!=0:
                cx.append(int(momentos['m10']/momentos['m00']))
                cy.append(int(momentos['m01']/momentos['m00']))
            contours.append(conta)

    test = cv2.drawContours(img,contours,-1,(255,255,0),thickness=2)
    cv2.imshow("contornos",test)
    return contours,cx,cy


def distToCenter(contours,cx,cy):
    corrected = []
    #maxima diferenca do raio calculado inicialmente e os pontos
    #provenientes dos contornos
    mx = 10
    counter =0
    #distance to center
    for x,y in zip(cx,cy):
        raio = np.sqrt(cv2.contourArea(contours[counter])/np.pi)
        raioThresholdPositive = raio+mx
        raioThresholdNegative = raio-mx
        currentContour = contours[counter]

        #CIRUCLARIDADE
        area = cv2.contourArea(currentContour)
        perimetro = cv2.arcLength(currentContour,True)
        circularidade = (4*np.pi*area)/(perimetro**2)

        if circularidade < 0.8:
            counter +=1
            continue

        filtered = filter(lambda f:
        True if (np.sqrt((f[0][0]-x)**2 + (f[0][1]-x)**2)>raioThresholdPositive
                    or np.sqrt((f[0][0]-x)**2 + (f[0][1]-x)**2)<raioThresholdNegative)
             else False, currentContour)
        corrected.append(np.asarray(filtered))
        counter+=1

    #filtrar arrays que estejam a 0
    corrected = filter(lambda a: len(a)!=0 ,corrected)
    corrected = np.asarray(corrected)

    return corrected

def classifica(array):
    valor=0
    for a in array:
        area = cv2.contourArea(a)
        for key,value in intervalos.iteritems():
            if(value[0]<= area < value[1]):
                valor += key
                break
    return valor


def classificador():

    # imagem ='P1.jpg' #WORKS
    # imagem ='P2.jpg' #WORKS
    # imagem ='P3.jpg' #WORKS less one coin
    # imagem ='P4.jpg' #WORKS
    # imagem ='P5.jpg' #WORKS
    # imagem ='P6.jpg' #WORKS
    # imagem ='P7.jpg' #WORKS
    # imagem ='P8.jpg' #WORKS
    # imagem ='P9.jpg' #WORKS
    imagem = "P1000712s.jpg"

    #leitura da imagem em tons de cinzento
    img = cv2.imread(imagem,cv2.IMREAD_COLOR)
    enhanced = brightEnhance(img)
    ib,ig,ir = cv2.split(enhanced)
    # cv2.imshow('Imagem Original',img)
    #smoothing a imagem - MELHORAMNETO
    melhorada = improveImage(ir)
    # cv2.imshow('Imagem Melhorada',melhorada)
    rt,thresh = imageBinary(melhorada)
    # cv2.imshow('Imagem Binarizada',thresh)
    #erosao
    workedImage = smoothImage(thresh)
    # cv2.imshow('Imagem Erodida',erode)
    #centroides
    contours,cx,cy = centroides(workedImage,img)
    #filtrar pontos que nao estao de acordo com o raio esperado
    final_areas = distToCenter(contours,cx,cy)
    valor = classifica(final_areas)
    cv2.waitKey(0)

    print "Valor final: " + str(valor)

if __name__ == "__main__":
    classificador()
