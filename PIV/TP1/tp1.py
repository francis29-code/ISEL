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
    return cv2.threshold(image,0,255,cv2.THRESH_TRIANGLE)

def smoothImage(image):
    #TRATAMENTO DA IMAGEM
    #structuring element - uma imagem binaria
    matriz = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9))
    #dilate melhor que o erode, imagens das moedas ficam mais redondas
    erode = cv2.erode(image,matriz,iterations=1)
    return erode

def centroides(image):
    #apanhar os contornos de uma imagem binaria
    contornos,hierarquia,lel = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    centroide = []
    cx = []
    cy = []
    for conta in hierarquia:
        if cv2.contourArea(conta) > 7000:
            momentos = cv2.moments(conta)
            #m00 equivale a area = cv2.contourArea(conta)
            if momentos['m00']!=0:
                cx.append(int(momentos['m10']/momentos['m00']))
                cy.append(int(momentos['m01']/momentos['m00']))
                centroide.append(conta)
    return centroide,cx,cy


def distToCenter(centroide,cx,cy):
    corrected = []
    #maxima diferenca do raio calculado inicialmente e os pontos
    #provenientes dos contornos
    mx = 10
    counter =0
    #distance to center
    for x,y in zip(cx,cy):
        classifica(cv2.contourArea(centroide[counter]))
        distref = np.sqrt(cv2.contourArea(centroide[counter])/np.pi)
        distref = distref+mx
        distref2 = distref-(2*mx)
        current = centroide[counter]
        filtered = filter(lambda f: True if (np.sqrt((f[0][0]-x)**2 + (f[0][1]-x)**2)>distref
        or np.sqrt((f[0][0]-x)**2 + (f[0][1]-x)**2)<distref2) else False, current)
        corrected.append(filtered)
        counter+=1

    return corrected

def classifica(area):
    global valor
    if(area>= 7000 and area<=10000):
        valor += moedas.get('0.01')
    if(area>= 11000 and area<12000):
        valor += moedas.get('0.02')
    if(area>= 14000 and area<=15000):
        valor += moedas.get('0.05')
    if(area>= 12000 and area<14000):
        valor += moedas.get('0.10')
    if(area> 15000 and area<=17000):
        valor += moedas.get('0.20')
    if(area> 19000 and area<=23000):
        valor += moedas.get('0.50')
    if(area> 17000 and area<=19000):
        valor += moedas.get('1.00')

def teste():

    #leitura da imagem em tons de cinzento
    img = cv2.imread('P1.jpg',cv2.IMREAD_GRAYSCALE)
    # cv2.imshow('Imagem Original',img)
    #smoothing a imagem - MELHORAMNETO
    melhorada = improveImage(img)
    # cv2.imshow('Imagem Melhorada',melhorada)
    #THRESH_TRIANGLE fica mais nitida - BINARIZACAO
    rt,thresh = imageBinary(melhorada)
    cv2.imshow('Imagem Binarizada',thresh)
    #erosao
    erode = smoothImage(thresh)
    cv2.imshow('Imagem Erodida',erode)
    #centroides
    centroide,cx,cy = centroides(erode)
    #filtrar pontos que nao estao de acordo com o raio esperado
    array_final = distToCenter(centroide,cx,cy)
    cv2.waitKey(0)

    print "Valor final: " + str(valor)

if __name__ == "__main__":
    teste()
