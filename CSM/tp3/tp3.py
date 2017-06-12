# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:06:13 2017

@author: joao_
"""

import numpy as np
from trab3Test import *
import cv2
import math
import matplotlib.pyplot as plt
from time import time
import os

def codificador_ex1(img):
    tam = img.shape
    array_final = np.array(img)
   
    for i in np.arange(0,tam[0],8): 
        for j in np.arange(0,tam[1],8):
            bloco = img[i:i+8,j:j+8]
            bloco_dct = cv2.dct(bloco)
            array_final[i:i+8,j:j+8] = bloco_dct     
    return array_final
    
def descodificador_ex1(dct):
    tam = img.shape
    array_final = np.array(img)
    
    for i in np.arange(0,tam[0],8): 
        for j in np.arange(0,tam[1],8):
            bloco = dct[i: i+8,j:j+8]
            inversa = cv2.dct(bloco,np.array(bloco),cv2.DCT_INVERSE)
            array_final[i:i+8,j:j+8] = inversa
    return array_final

'''
    Função codificador que efetua a DCT bidimensional
'''
def DCT(img,Q,per):
    tam = img.shape
    array_final = np.array(img)
    fator_compressao = np.multiply(Q,quality_factor(per))
    
    for i in np.arange(0,tam[0],8): 
        for j in np.arange(0,tam[1],8):
            bloco = img[i:i+8,j:j+8] 
            bloco_dct = cv2.dct(bloco)
            quantificacao = np.round(np.divide(bloco_dct, fator_compressao))
            array_final[i:i+8,j:j+8] = quantificacao     
    return array_final

'''
    Função descodificador que efetua a DCT inversa
'''
def IDCT(img,Q,per):
    tam = img.shape
    array_final = np.array(img)
    fator_compressao = np.multiply(Q,quality_factor(per))

    for i in np.arange(0,tam[0],8): 
        for j in np.arange(0,tam[1],8):
            bloco = img[i: i+8,j:j+8]
            bloco_dct = np.round(np.multiply(bloco, fator_compressao))
            inversa = cv2.dct(bloco_dct,np.array(bloco_dct),cv2.DCT_INVERSE)
            array_final[i:i+8,j:j+8] = inversa
    return array_final
    
'''
    Codificador que permite fazer a codificação diferencial dos coeficientes
    DC.
'''
def codificacao_dc(dct, K):
    tam = dct.shape
    final = []
    coef_DC_anterior = 0
    
    for lin in np.arange(0,tam[0],8): 
        for col in np.arange(0,tam[1],8): 
            bloco = dct[lin:lin+8,col:col+8]
            diferenca = bloco[0][0] - coef_DC_anterior
            
            if diferenca < 0:
                bin_neg = bin(int(diferenca))[2:]
                bin_dif = Complemento(bin_neg)
            else:
                if(diferenca != 0):
                    bin_dif = bin(int(diferenca))[2:]
            
            if(bin_dif != None):
                grandeza = len(bin_dif)
                bin_grandeza = K[grandeza]
                
            if(bin_grandeza != None):
                codificado = bin_grandeza + bin_dif
            else:
                codificado = K[0]
            
            bin_dif = None
            bin_grandeza = None
            final.append(codificado)
            coef_DC_anterior = bloco[0][0]
    
    return final
    
''' Descodificação dos componentes DC '''    
def descodificacao_dc(array,K, altura, largura):
    final = np.zeros((altura/2)*(largura/2))
    posSeg = 0
    pos = 0
    
    while posSeg < len(array):
        for grandeza,binario in K.items():
            if array[posSeg:posSeg+len(binario)] == binario:
                bit = array[posSeg+len(binario):posSeg+len(binario)+grandeza]
                
                if grandeza == 0:
                    final[pos] = (0)
                
                if grandeza != 0 and bit[0] == "0":
                    final[pos] = ((-(int(Complemento(bit),2))))
                
                if grandeza != 0 and bit[0] == "1":
                    final[pos] = ((int(bit,2)))
                
                posSeg += len(binario)+grandeza
                pos += 1
                break
      
    final = final.reshape(len(final),)
    for i in range(len(final)-1):
        final[i+1] = final[i]+final[i+1]
        
    return final
    
''' Codificação dos componentes AC '''   
def codificacao_AC(dct,ind_zz,K5):
    final = []
    tam = dct.shape           

    for linha in np.arange(0,tam[0],8): 
        for coluna in np.arange(0,tam[1],8):  
            bloco = dct[linha:linha+8,coluna:coluna+8]
            Bloco = bloco.flatten(order='F')
            copia = Bloco[ind_Z]
  
            posSeg = 0
            zeros = 0
            EOB = True
            
            while(EOB):
                if(sum(abs(copia[posSeg:]))==0):
                    bin_EOB = K5[(0, 0)]
                    final.append(bin_EOB)
                    EOB = False
                    break
                elif(zeros>15):
                    posSeg -= 1
                    cod_huffman = K5[(15,0)]
                    final.append(cod_huffman)
                    zeros = 0    
                elif(copia[posSeg] == 0):
                    zeros += 1
                    posSeg += 1
                else:
                    if(copia[posSeg]<0):
                        bin_neg = bin(int(copia[posSeg]))[2:]
                        amplitude_bin = Complemento(bin_neg)        
                    else:
                        amplitude_bin = bin(int(copia[posSeg]))[2:]
                    
                    grandeza = len(amplitude_bin)    
                    cod_huffman = K5[(zeros,grandeza)]
                    codigo_huffman_AC = cod_huffman + amplitude_bin    
                    final.append(codigo_huffman_AC)
                    zeros = 0
                    posSeg += 1

    return final
    
''' Descodificação dos componenetes AC '''
def descodificacao_AC(array_rec,K5,altura,largura):
    array = ''.join(array_rec)
    final = np.zeros(8*8)
    
    posSeg = 0
    pos = 0
    array_blocos = np.zeros(shape=(altura,largura))
    linha = 0
    coluna = 0
    
    while posSeg < len(array):
        
        for par_valores, binarios in K5.items():
            if array[posSeg:posSeg + len(binarios)] == binarios:
                run = par_valores[0]
                ampl = par_valores[1]
                
                pos += run
                posSeg += len(binarios)
                
                if(run == 0 and ampl == 0):
                    if(coluna == largura):
                        coluna = 0
                        linha += 8
                       
                    array_blocos[linha:linha+8,coluna:coluna+8] = final.reshape(8,8)

                    coluna += 8
                    
                    final = np.zeros(8*8)
                    pos = 0
                    
                elif(run!=15 and ampl!=0) or (run!=0 and ampl!=0):
                    bin_conv = array[posSeg:posSeg+ampl]
                    
                    if bin_conv[0] == "0":
                        final[pos] = -(int(Complemento(bin_conv),2))
                    else:
                        final[pos] = int(bin_conv,2)
                    
                    pos += 1
                    posSeg += ampl

                break

    return array_blocos
    
''' Codificação '''    
def codifica(img, fator_q, filename):
    altura, largura = img.shape
    dct = DCT(img, Q, fator_q)
    dc = codificacao_dc(dct, K3)
    len_dc = len(''.join(dc))
    ac = codificacao_AC(dct, ind_Z, K5)
    dcac = ac + dc
    arrayJunto = ''.join(dcac)
    array = list(map(int,arrayJunto)) 
    
    count = 0
    while(len(array) % 8 != 0):
        array.append(0)
        count += 1

    array = np.array(array)
    arrayNovo = array.reshape(-1,8)
    decimais = convBi(arrayNovo)
    array_char = ['' for i in range(len(decimais)+7)]
    j = 7
    for i in decimais:
        a = chr(i)
        array_char[j] = a
        j += 1
    
    array_char[0] = str(count) 
    array_char[1] = str(len(str(largura))) 
    array_char[2] = str(len(str(altura)))
    array_char[3] = str(len(str(len_dc)))
    array_char[4] = str(largura)
    array_char[5] = str(altura) 
    array_char[6] = str(len_dc) 
    
    ficheiro = open(filename,"wb")
    for i in array_char:
        ficheiro.write(i)
    
    ficheiro.close()
    
''' Descodificação '''
def descodifica(filename, fator_qualidade):
    ficheiro = open(filename, "rb")
    stream = ficheiro.read()
    ficheiro.close()
    
    count = int(stream[0])
    tamanho_largura = int(stream[1])
    tamanho_altura = int(stream[2])
    tamanho_dc = int(stream[3])
    
    largura = int(stream[4:4+tamanho_largura])
    altura = int(stream[4+tamanho_largura:4+tamanho_altura+tamanho_largura])
    tam_dc = int(stream[4+tamanho_altura+tamanho_largura:4+tamanho_altura+tamanho_largura+tamanho_dc])
        
    st = stream[4+tamanho_altura+tamanho_largura+tamanho_dc:]
    array = ['' for i in range(len(st))]
    j = 0
    for i in st:
        array[j] = ord(i)
        j += 1
    
    binarios = convInt(array, 8)
    binarios = np.array(binarios).ravel()
    binarios = ''.join(binarios)
    
    if count == 0:
        binarios = binarios
    else:
        binarios = binarios[:-(count)]
    
    dcs = binarios[-(tam_dc):]
    
    descod_dcs = descodificacao_dc(dcs, K3, altura, largura)
    
    acs = binarios[:len(binarios)-len(dcs)]
    
    descod_acs = descodificacao_AC(acs, K5, altura, largura)
    
    inverso_acs = inv_zigzag(descod_acs)
    acsdcs = DCAC(descod_dcs, inverso_acs)  
    array_final = IDCT(acsdcs, Q, fator_qualidade)
    
    return array_final
    
def DCAC(codDC, codAC):
    tam = codAC.shape
    x = 0
    
    for lin in np.arange(0,tam[0],8): 
        for col in np.arange(0,tam[1],8): 
            bloco = codAC[lin:lin+8,col:col+8]
            bloco[0][0] = codDC[x]
            codAC[lin:lin+8,col:col+8] = bloco
            x += 1
    
    return codAC
    
''' Métodos auxiliares '''
def inv_zigzag(matriz):
    tam = matriz.shape
    blocos = np.array(matriz)
    for lin in np.arange(0,tam[0],8): 
        for col in np.arange(0,tam[1],8):  
            bloco = matriz[lin:lin+8,col:col+8].flatten()
            bloco_zz = bloco[ind_O].reshape((8,8),order='F')
            blocos[lin:lin+8,col:col+8] = bloco_zz
    return blocos
    
def Complemento(b):
    c = []
    for num in b:
        if num == '1': 
            c.append('0')
        elif num == '0': 
            c.append('1')
    bit = ''.join(c)
    return bit
    
def convBi(B):
    I = []
    decimal = 0
    for i in B:
        i = i[::-1]
        mult = 1
        decimal = 0
        for n in range(len(i)):
            decimal += int(i[n])*mult
            mult = mult * 2  
        I.append(decimal) 
    return I

def convInt(I, NB=0):
    B = []
    for i in I:
        aux = ""
        while (i > 0):
            aux = str(i%2) + aux
            i = i >> 1
        if NB != 0 and NB > len(aux):
            extra = NB - len(aux)
            aux = "0" * extra + aux  
        B.append(aux)
    return B
    
def SNR(original,descodificada):
    imageO = original.ravel()
    noise = original.astype(float) - descodificada.astype(float)
    imageA = noise.ravel()

    pOriginal = np.sum(imageO**2.)
    pdescodificada = np.sum(imageA**2.)
    SNR = 10*np.log10(pOriginal/pdescodificada)

    return round(SNR,2)
    
def taxa_compressao(original,descodificada):
    sizeO = os.path.getsize(original)
    sizeA = os.path.getsize(descodificada)
    ratio = float(sizeO)/float(sizeA)

    return round(ratio,2)

''' Funções que permitem responder ao enunciado do trabalho prático '''

def ex1(img, diretoriaEX1):
    dct = codificador_ex1(img)
    idct = descodificador_ex1(dct)
    cv2.imwrite(diretoriaEX1 + "dct.tif", dct)
    cv2.imwrite(diretoriaEX1 + "idct.tif", idct)
    
 
def ex2(img,diretoriaEX2):
    print "EXERCICIO 2"
    fator_qualidade = 25
    dct = DCT(img,Q,fator_qualidade)
    idct = IDCT(dct,Q,fator_qualidade)
    print 'SNR ' + str(fator_qualidade)+ ':', SNR(img,idct)
    cv2.imwrite(diretoriaEX2 + "DCT_" + str(fator_qualidade) + ".tiff", dct)
    cv2.imwrite(diretoriaEX2 + "IDCT_" + str(fator_qualidade) + ".tiff", idct)
    
    fator_qualidade = 50
    dct = DCT(img,Q,fator_qualidade)
    idct = IDCT(dct,Q,fator_qualidade)
    print 'SNR ' + str(fator_qualidade)+ ':', SNR(img,idct)
    cv2.imwrite(diretoriaEX2 + "DCT_" + str(fator_qualidade) + ".tiff", dct)
    cv2.imwrite(diretoriaEX2 + "IDCT_" + str(fator_qualidade) + ".tiff", idct)
    
    fator_qualidade = 75
    dct = DCT(img,Q,fator_qualidade)
    idct = IDCT(dct,Q,fator_qualidade)
    print 'SNR ' + str(fator_qualidade)+ ':', SNR(img,idct)
    cv2.imwrite(diretoriaEX2 + "DCT_" + str(fator_qualidade) + ".tiff", dct)
    cv2.imwrite(diretoriaEX2 + "IDCT_" + str(fator_qualidade) + ".tiff", idct)
    print "-------------------------------------------------------------------"
    
def ex7(img, diretoriaEX7):
    
    print "EXERCICIO 7"
    # Qualidade 25%
    print "Fator de qualidade de 25%:"
    fator_qualidade = 10
    filename = "ficheiro_" + str(fator_qualidade) + ".txt"
    img_out_name = diretoriaEX7 + "desc_" + str(fator_qualidade) + ".tiff"
    t0c = time()
    codifica(img,fator_qualidade,filename)
    t1c = time()
    print "Tempo codificação: " , round(t1c - t0c,2)
    t0d = time()
    desc = descodifica(filename, fator_qualidade)
    t1d = time()
    print "Tempo descodificação: " , round(t1d - t0d, 2)
    cv2.imwrite(diretoriaEX7 + "desc_" + str(fator_qualidade) + ".tiff", desc)
    snr_25 = SNR(img,desc)
    print 'SNR: ', snr_25
    taxa_comp_25 = taxa_compressao("files/lena.tif", img_out_name)
    print 'Taxa Compressão: ' , taxa_comp_25
    print " "
    
    # Qualidade 50%
    print "Fator de qualidade de 50%:"
    fator_qualidade = 50
    filename = "ficheiro_" + str(fator_qualidade) + ".txt"
    img_out_name = diretoriaEX7 + "desc_" + str(fator_qualidade) + ".tiff"
    t0c = time()
    codifica(img,fator_qualidade,filename)
    t1c = time()
    print "Tempo codificação: " , round(t1c - t0c,2)
    t0d = time()
    desc = descodifica(filename, fator_qualidade)
    t1d = time()
    print "Tempo descodificação: " , round(t1d - t0d,2)
    cv2.imwrite(img_out_name, desc)
    snr_50 = SNR(img,desc)
    print 'SNR: ', snr_50
    taxa_comp_50 = taxa_compressao("files/lena.tif", img_out_name)
    print 'Taxa Compressão: ' , taxa_comp_50
    print " "
    
    # Qualidade 75%
    print "Fator de qualidade de 75%:"
    fator_qualidade = 75
    filename = "ficheiro_" + str(fator_qualidade) + ".txt"
    img_out_name = diretoriaEX7 + "desc_" + str(fator_qualidade) + ".tiff"
    t0c = time()
    codifica(img,fator_qualidade,filename)
    t1c = time()
    print "Tempo codificação: " , round(t1c - t0c,2)
    t0d = time()
    desc = descodifica(filename, fator_qualidade)
    t1d = time()
    print "Tempo descodificação: " , round(t1d - t0d,2)
    snr_75 = SNR(img,desc)
    print 'SNR: ', snr_75
    taxa_comp_75 = taxa_compressao("files/lena.tif", img_out_name)
    print 'Taxa Compressão: ' , taxa_comp_75
    cv2.imwrite(img_out_name, desc)
    print " "
    
    # Gráficos
    snrs = [snr_25,snr_50,snr_75]
    taxas = [taxa_comp_25, taxa_comp_50, taxa_comp_75]    
    plt.title("Taxa de compressao em funcao da SNR: ")
    plt.plot(snrs,taxas, 'r')
    plt.xlabel("SNR")
    plt.ylabel("Taxa de compressao")
    plt.grid(color='r', linestyle='-', linewidth=0.5)
    plt.show()
    
    
if __name__== "__main__":
    diretoria = "files/"
    nome_img = "Lena.tif"
    diretoriaEX1 = diretoria + "ex1/" 
    diretoriaEX2 = diretoria + "ex1ex2/"
    diretoriaEX7 = diretoria + "ex7/"
    filename = diretoria + "ficheiro"
    
    img = cv2.imread(diretoria + nome_img, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    img = np.array(img, dtype = np.float64)
    
    ex1(img, diretoriaEX1)
    ex2(img, diretoriaEX2)
    ex7(img, diretoriaEX7)
    