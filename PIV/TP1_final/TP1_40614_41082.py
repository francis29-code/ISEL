# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 23:03:11 2016

@author: Hugo Safara
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

def canalRGB(image):
    histogramaB = cv2.calcHist([image], [0] , None, [256], [0,256])
    histogramaG = cv2.calcHist([image], [1] , None, [256], [0,256])
    histogramaR = cv2.calcHist([image], [2] , None, [256], [0,256])

#    plt.plot(histogramaB)
#    plt.plot(histogramaG)
#    plt.plot(histogramaR)

    ib,ig,ir = cv2.split(image)
    return ib,ig,ir


def melhoramento_imagem(image):
    melhoramento = cv2.bilateralFilter(image, 22, 30, 30)
    return melhoramento

def binarizacao_imagem(imagem_filtrada):
    ret,thresh = cv2.threshold(imagem_filtrada, 0, 255, cv2.THRESH_OTSU)
    return ret,thresh

def tratamento_imagem(imagem_binarizada):
   matriz = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
   erosao = cv2.erode(imagem_binarizada, matriz,iterations = 3)
   return erosao

def find_contours(imagem_tratada):
    cenas,contornos,hierarquia = cv2.findContours(imagem_tratada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #filtra-se todos os contornos que tenham contornos dentro deles.
    array =[]
    for x in range(len(hierarquia[0])):
        if((hierarquia[0][x][2]!=-1) or((hierarquia[0][x][3]!=-1))):
            array.append(x)

    array.sort(reverse=True)

    for i in array:
        contornos.pop(i)
    return contornos

def centroide(imagem_com_contornos,min_coin_area):
    centroide = []
    cx = []
    cy = []

    for conta_x in imagem_com_contornos:
        if cv2.contourArea(conta_x) > min_coin_area:
            M = cv2.moments(conta_x)

            if M['m00']!=0:
                cx.append(int(M['m10']/M['m00']))
                cy.append(int(M['m01']/M['m00']))

            centroide.append(conta_x)
    return centroide,cx,cy

def distancia_centro(array_centroide,cx,cy):
    aux = []
    for x in range(len(array_centroide)):
        ditancia_considera_x = array_centroide[x][50][0][0]
        ditancia_considera_y = array_centroide[x][50][0][1]
        distancia_ref = math.sqrt((ditancia_considera_x - cx[x])**2 + (ditancia_considera_y - cy[x])**2)
        for y in range(len(array_centroide[x])):
            dis_x = array_centroide[x][y][0][0]
            dis_y = array_centroide[x][y][0][1]
            distancia = math.sqrt((dis_x - cx[x])**2 + (dis_y - cy[x])**2)
            if ((distancia<distancia_ref-15) or (distancia>distancia_ref+15)):
                aux.append(x)
                break
   #filtragem de objectos relativamente à distancia de certos pontos ao centro de um objecto em questao.
    array_final = []
    for x in range(len(array_centroide)):
        for h in aux:
            if(x == h):
                array_centroide[x] = "n"
        if (array_centroide[x]!="n"):
            array_final.append(array_centroide[x])

    return array_final

def area_contorno(imagem_objectos,min_coin_area):
    area_contorno = []

    for x in imagem_objectos:
        if cv2.contourArea(x) > min_coin_area:
            area_contorno.append(cv2.contourArea(x))
    return area_contorno

def array_To_String(array_area_find,distancia):

    print('Número de moedas: ' + str(len(distancia)))
    print('As moedas existentes em cima da mesa são de:')

    string = []
    for area in range(len(array_area_find)):
        if(array_area_find[area]>= 7000 and array_area_find[area]<=10000):
            string.append(0)
        if(array_area_find[area]>= 11000 and array_area_find[area]<12000):
            string.append(1)
        if(array_area_find[area]>= 14000 and array_area_find[area]<=15000):
            string.append(2)
        if(array_area_find[area]>= 12000 and array_area_find[area]<14000):
            string.append(3)
        if(array_area_find[area]> 15000 and array_area_find[area]<=17000):
            string.append(4)
        if(array_area_find[area]> 19000 and array_area_find[area]<=23000):
            string.append(5)
        if(array_area_find[area]> 17000 and array_area_find[area]<=19000):
            string.append(6)

    string = sorted(string)

    valor = 0
    for stri in range(len(string)):
        if(string[stri]==0):
            valor += 0.01
            print('0,01€')
        if(string[stri]==1):
            valor += 0.02
            print('0,02€')
        if(string[stri]==2):
            valor += 0.05
            print('0,05€')
        if(string[stri]==3):
            valor += 0.10
            print('0,10€')
        if(string[stri]==4):
            valor += 0.20
            print('0,20€')
        if(string[stri]==5):
            valor += 0.50
            print('0,50€')
        if(string[stri]==6):
            valor += 1
            print('1€')

    print("Quantia total: " + str(valor) + "€")
    return ""


if __name__ == "__main__":

    image = cv2.imread('P9.jpg')
    cv2.imshow("Imagem Original",image)

    min_coin_area = 7000

    canal_RGB = canalRGB(image)
    melhoramento = melhoramento_imagem(canal_RGB[2])
    binarizacao = binarizacao_imagem(melhoramento)
    tratamento = tratamento_imagem(binarizacao[1])
    encontra_contornos = find_contours(tratamento)
    centroide,cx,cy = centroide(encontra_contornos,min_coin_area)
    distancia = distancia_centro(centroide,cx,cy)
    area_find = area_contorno(distancia,min_coin_area)
    array_To_String(area_find,distancia)
