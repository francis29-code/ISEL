import cv2
import numpy as np
import matplotlib.pyplot as plt
import math


def teste():

    #leitura da imagem em tons de cinzento
    img = cv2.imread('P1.jpg',cv2.IMREAD_GRAYSCALE)

    #smoothing a imagem - MELHORAMNETO
    melhorada = cv2.bilateralFilter(img,22,30,30)

    #THRESH_TRIANGLE fica mais nitida - BINARIZACAO
    rt,thresh = cv2.threshold(melhorada,0,255,cv2.THRESH_TRIANGLE)

    #TRATAMENTO DA IMAGEM
    #structuring element - uma imagem binaria
    matriz = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
    #dilate melhor que o erode, imagens das moedas ficam mais redondas
    erode = cv2.erode(thresh,matriz,iterations=1)

    #apanhar os contornos de uma imagem binaria
    contornos,hierarquia,lel = cv2.findContours(erode,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(img,contornos,0,(0,255,0),cv2.FILLED,8,hierarquia[0])
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

    aux = []
    #maxima diferenca do raio calculado inicialmente e os pontos
    #provenientes dos contornos
    threshold_maximo = 10
    counter =0
    #distance to center
    print centroide[0] #array
    print "1" + str(centroide[0][0])        #primeiro ponto
    print "2" + str(centroide[0][0][0])     #tuplo
    print "3-" + str(centroide[0][0][0][0]) #x
    print "4-" + str(centroide[0][0][0][1]) #y

    for x,y in zip(cx,cy):
        distref = np.sqrt(cv2.contourArea(hierarquia[counter])/np.pi)
        current = hierarquia[counter]

        print cal




        break



    #hierarquia sao o numero de figuras encontradas com o structuring element
    #definido na dilataao da imagem
    # new_contornos = [(lambda x: True if any(x)!=False else False)(x) for x in hierarquia[0]]
    # new_contornos = [x for x in hierarquia: if ]

    # cv2.imshow("thresholded",erode)
    # cv2.waitKey(0)

if __name__ == "__main__":
    teste()
