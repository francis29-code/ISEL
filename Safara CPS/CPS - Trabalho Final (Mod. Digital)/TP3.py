# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:11:44 2015

@author: Hugo Safara
"""

from TP2_2 import codificacao
from TP2_1 import quantificacao
from TP2_1 import tabelas,SNR
from TP1 import amostragem
import numpy as np
import numpy
import scipy.io.wavfile as wav
numpy.set_printoptions(threshold=numpy.nan)


A = 20005.0
f = 3014.0
Fs = 8000
Ts = 1./Fs
R = 3
fs, data = wav.read('som_8_16_mono.wav')
z = max(data)
t,sinal = amostragem(A,0.0,1.0,Ts)
T = tabelas(z,R)
sinal_quant,indices = quantificacao(data,T[0],T[1])
sinal_cod = codificacao(indices,R)
#print sinal_cod

def Hamming(sinal_cod):

    I = np.array(np.identity(11))

    P = np.array([[1.,1.,1.,1.],[0.,1.,1.,1.],[1.,0.,1.,1.],[1.,1.,0.,1.],
         [1.,1.,1.,0.],[0.,0.,1.,1.],[0.,1.,0.,1.],[0.,1.,1.,0.],
         [1.,0.,1.,0.],[1.,0.,0.,1.],[1.,1.,0.,0.]])
  
    G = np.hstack((I,P))

    if(len(sinal_cod)%11!=0):
        z = 11-len(sinal_cod)%11  
        y = np.zeros(z)
        sinal_cod.extend((y))
        
    lista = np.zeros((len(sinal_cod)/11)*15)
    
    count = 0
    for i in range(0,len(sinal_cod),11):
        ham = np.dot(sinal_cod[i:i+11],G)%2  
        lista[i+count:i+count+15] = ham
        count += 4
    return lista


def Hamming_correcao(mensagem):
    
    if(len(mensagem)%15!=0):
        resultado = 15 - len(mensagem)%15
        mensagem = np.append(mensagem,np.zeros(resultado))

    P = np.array([[1.,1.,1.,1.],[0.,1.,1.,1.],[1.,0.,1.,1.],[1.,1.,0.,1.],
         [1.,1.,1.,0.],[0.,0.,1.,1.],[0.,1.,0.,1.],[0.,1.,1.,0.],
         [1.,0.,1.,0.],[1.,0.,0.,1.],[1.,1.,0.,0.],[1.,0.,0.,0.],[0.,1.,0.,0.],
         [0.,0.,1.,0.],[0.,0.,0.,1.]])
        
    numErros=0
    aux=0
    count = 0
    bits = np.zeros((len(mensagem)/15)*11)
    for x in np.arange(0,len(mensagem),15):
        y = np.dot(mensagem[x:x+15],P)%2
        for z in range(len(P)):
            if(sum(P[z]==y)==4):
                mensagem[x+aux] = (mensagem[x+aux]+1)%2
                break;
            else:
                aux+=1
        if(sum(y)!=0):
            numErros+=1
        aux=0
        bits[count:count+11] = mensagem[x:x+11]
        count+=11
    return bits,numErros  
   
#bits = [1.,0.,0.,0.,0.,1.,0.,0.,0.,1.,1.,1.,0.,0.,0.]
#print len(bits)
x = Hamming(sinal_cod)

var = sinal_cod[0:11]
y = Hamming_correcao(x)
#print y
#print("Sinal codificado:")
#print var
#print("Hamming:")
#print x[0:15]

#print len(x)
#print sinal_cod[0:20]
#print len(sinal_cod) 
#num_erros = 800.0
#bert = (num_erros/len(x))
##  
#erro = np.random.binomial(1, bert, len(x))
#num = 8000



#print len(sinal_cod)
#BER = 0.1
#erro = 1*np.logical_xor(x, np.random.binomial(1,BER, len(x)))
##
#simulador = 1 * \
# (np.logical_xor(x, erro))
##print("apos Hamming") 
##print simulador[0:15]
#z = Hamming_correcao(erro)
##print len(z)
##print("Correcao")
##print z[0:11]
##print len(sinal_cod)
#simulador2 = 1 * \
# (np.logical_xor(sinal_cod, z))
##print("Bits que nao se corrigiram")
#x = np.sum(simulador2)
#print x
#sin = len(sinal_cod)
#y = x/sin
#print y