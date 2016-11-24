# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 01:41:36 2015

@author: Hugo Safara
"""

from TP3 import Hamming, Hamming_correcao
from TP2_2 import codificacao,descodificacao
from TP2_1 import quantificacao,quantificacao_inversa
from TP2_1 import tabelas,SNR
from TP1 import amostragem
import scipy.io.wavfile as wav
from scipy.special import erfc
import numpy as np
import matplotlib.pyplot as plt
import pylab as pylab
import time

def QAM_16(array,P,Eb):
    y = array.astype(int)

    lista = ""
    
    for h in range(len(y)):
        lista = lista + str(y[h])

    array_int = []

    for i in range(0, len(lista), 4):
        array_int.append(int(lista[i:i+4],2))

    aux      = 0
    contador = 0
    sin_QAM  = np.zeros(len(array)/4.0*P)

    if(len(sin_QAM)%8!=0):
        z = 8-(len(sin_QAM)%8)
        sin_QAM = np.ones(len(array)/4.0*P+z)


    for g in range(len(array_int)):
        x = array_16QAM[array_int[aux]][0]
        y = array_16QAM[array_int[aux]][1]
        aux = aux + 1

        sin_cos = x*np.cos(2*np.pi*fp*T2) + y*np.sin(2*np.pi*fp*T2)

        sin_QAM[contador:contador+8] = sin_cos
        contador = contador + 8       
    return(sin_QAM)

    
def constelation(sinal_q):          
    for z in range(0,len(sinal_q)-1,2):
        plt.plot(sinal_q[z],sinal_q[z+1],"o")        
        plt.grid()
        plt.show()
        pylab.xlim([-4,4])                    
        pylab.ylim([-4,4])
        
def AWGN(sinal_entrada, potencia):
    sinal_out_com_array = sinal_entrada + np.sqrt(potencia)*\
                          np.random.randn(1, len(sinal_entrada))
                          
    sinal_out = sinal_out_com_array[0]
    
    return(sinal_out)
    
def des_QAM_16(sinal):
    if(len(sinal)%8!=0):
        res = 8 - len(sinal)%8
        sinal = np.append(sinal,np.ones(res))
        
    array_referencial = [-4*E0,-2*E0,0*E0,2*E0,4*E0]
    novo_array        = [-3E0,-3*E0,-E0,E0,3E0,3E0]
    array_des_QAM     = np.ones(len(sinal)/2.0)

    ArrayBits = [[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],\
                 [0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],\
                 [1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],\
                 [1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]   
                 
    contador = 0
    
    
    for s in range(0, len(sinal),8):
        
        retorna_x = sum(sinal[s:s+8]*np.cos(2*np.pi*fp*T2))/4.0
        retorna_y = sum(sinal[s:s+8]*np.sin(2*np.pi*fp*T2))/4.0
                 
        somatorio_x = novo_array[sum(retorna_x >array_referencial)]
        somatorio_y = novo_array[sum(retorna_y >array_referencial)]
        
        aux = [somatorio_x,somatorio_y]
        
        find_num = array_16QAM.index(aux)

        array_des_QAM[contador:contador+4] = \
        array_des_QAM[contador:contador +4]*np.asarray(ArrayBits[find_num])
        
        contador = contador +4
        
    return (array_des_QAM)     


if __name__ == "__main__":
    
    print("Inicio do main")
    print(" ")
    
    A = 20005.0
    f = 3014.0
    Fs = 8000.0
    Ts = 1./Fs
    R = 8
    t,sinal = amostragem(A,0.0,1.0,Ts)
    tempo2 = time.time()
    fs, data = wav.read('gravacao.wav')
    z = max(data)
    T = tabelas(z,R)
    sinal_quant,indices = quantificacao(data,T[0],T[1])
    sinal_cod = codificacao(indices,R)
    ham = Hamming(sinal_cod)
    P  = 8.0
    T2  = np.arange(8)
    fp = 2.0/P      

    Pot = 4.0 
    E0=1.
    array_16QAM = [[-3E0,3E0],[-E0,3E0],[E0,3E0],[3E0,3E0],\
                   [-3E0,E0],[-E0,E0],[E0,E0],[3E0,E0],[-3E0,-E0],\
                   [-E0,-E0],[E0,-E0],[3E0,-E0],[-3E0,-3E0],[-E0,-3E0],\
                   [E0,-3E0],[3E0,-3E0]]   


#    Qam = QAM_16(ham,P,0.75)
#    awgn = AWGN(Qam,Pot)
#    des = des_QAM_16(awgn)
#    des1 = des.astype(int)
#    det_erro,erros = Hamming_correcao(des1)
#
#    if(len(sinal_cod)!=len(det_erro)):
#        sinal_cod = np.append(sinal_cod,np.zeros(len(det_erro)-len(sinal_cod)))
#
#    BER_pratico_antes_ham = 1 * \
#    (np.logical_xor(sinal_cod, det_erro))
#
#    BER_pratico_antes_ham2 = np.sum(BER_pratico_antes_ham)/float(len(det_erro))
#
#    BERsc = float(erros)/float(len(det_erro))
#    BER_teorico_antes_ham = ((3.0*14.0)/2.0)*(BERsc**2.0)
#
#    BER_pratico_apos_ham = 1 * \
#    (np.logical_xor(np.append(ham,np.zeros(1)), des))
#
#    BER_pratico_apos_ham2 = np.sum(BER_pratico_apos_ham)/float(len(des))
#
#    BER_teorico_apos_ham = (2.0/4.0)*(1.0-(1.0/np.sqrt(16.0)))*erfc(np.sqrt((3.0*4.0)/(2.0*(16.0-1.0))*(0.75/Pot)))
#
#    descod = descodificacao(det_erro.astype(int),R)
#    descod2 = descod.astype(int)
#    desquant = quantificacao_inversa(descod,T[0])
#    desquant2 = desquant.astype(int)
#    SNR = SNR(z,R,desquant2)
#
#    wav.write('som_fim_Pot_3.7_(som_mono).wav', fs, desquant2.astype('int16'))

    print(" ")    
    print("Fim do main")
