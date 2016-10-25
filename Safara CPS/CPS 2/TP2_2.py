# -*- coding: utf-8 -*-
"""
Created on Wed Nov 04 23:03:13 2015

@author: Hugo Safara
"""

from TP1 import amostragem
from TP2_1 import quantificacao
from TP2_1 import tabelas
from TP2_1 import SNR
import scipy.io.wavfile as wav
import numpy as np

def codificacao(indice,R):
    array = []
    for x in range(len(indice)):
        binario = indice[x]+2**R
        binario = binario.astype(int)
        corte = map(int,bin(binario)[3:])
        array = array + corte
    return array

def descodificacao(array_bin,r):
    lista = ""
    
    for h in range(len(array_bin)):
        lista = lista + str(array_bin[h])
        
    array_int = np.zeros(np.ceil(len(lista)/float(r)))
    aux = 0
    for x in range(0,len(lista),r):
        array_int[aux] = int(lista[x:x+r],2)
        aux = aux+1
    return array_int

if __name__ == "__main__":
    
    print("Inicio do main")
    print(" ")
    
    A = 20000.0
    f = 3014.0
    Fs = 8000
    Ts = 1./Fs

    t,sinal = amostragem(A,0.0,1.0,Ts)
    fs, data = wav.read('gravacao.wav')


############################## Exercicio 2 ####################################
##    R = 5
#    R = [3.,5.,8.]
# 
#    z = max(data)
#    
#    for x in range(len(R)):
#        SNR(z,R[x],data)
#        
#    T = tabelas(z,R)
#    quant,ind = quantificacao(data, T[0], T[1])  
#    cod = codificacao(ind,R)
#    descod = descodificacao(cod,R)

    print(" ")    
    print("Fim do main")