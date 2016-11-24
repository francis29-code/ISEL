# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:36:01 2015

@author: Rita
"""
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import pylab as pylab
from TP1 import gravar

        
#ex1
def tabelas(Vmax, R):                        #R - nº de bits por amostra
    L = 2**R                                 # L- nª intervalos de quantificação
    deltaQ = 2.*Vmax/L 
    valD =np.arange(-Vmax, Vmax+deltaQ, deltaQ)
    valQ = np.arange(-Vmax+deltaQ/2, Vmax, deltaQ)    
    return valQ,valD
    

#ex2
def quantificacao(sinal, valoresQ, intervalos):                        
     xq = np.zeros(len(sinal))
     indices = np.zeros(len(sinal))
     
     for i in range(len(sinal)):
         numero_de_valores = intervalos >= sinal[i]
         
         resultado = np.nonzero(numero_de_valores)
         xq2 = resultado[0][0]-1
         xq[i] = valoresQ[xq2]
         indices[i] = xq2
     return xq,indices

def quantificacao_inversa(valQ,valoresQ):
    result = np.arange(len(valQ))
    
    for i in range(len(valQ)):
        result[i] = valoresQ[valQ[i]]
        
    return (result)
    
#ex3
def SNR(A,R,sinal):
    pot_sinal = (np.sum(1.*np.power(sinal,2.0))/(len(sinal)))
    pot = (3.0*pot_sinal)/(np.power(A,2.))
    T = tabelas(A,R)
    quant_geral,_ = quantificacao(sinal, T[0], T[1])
    erro = sinal - quant_geral
    pot_erro = (np.sum(1.*np.power(erro,2.)/len(erro)))
    SNR_teorico = (6*R)+10*np.log10(pot)
    SNR_pratico = 10.0 * np.log10((pot_sinal)/(pot_erro))
    print "SNR Teórica = ", SNR_teorico 
    print "SNR Prático = ", SNR_pratico
    
if __name__ == "__main__":
    
    print("Inicio do main")
    print(" ")

    A = 20000.0
    f = 3014.0
    Fs = 8000.
    Ts = 1./Fs                          #frequencia de amostragem

    num_amostras = Fs
    passo = A*2/(num_amostras)                                      
    sinal = np.arange(-A,A,passo)

    fs, data = wav.read('gravacao.wav')
    
############################## Exercicio 3a) ##################################
#    A = 20006.0
    T = tabelas(A,3)
    #print T
#    t = np.arange(0.,1.,Ts)
#    plt.subplot(211)
#    plt.plot(t,sinal)
#    plt.ylabel('Amplitude')
#    plt.title('Amostragem do Sinal')
    sinal_quantificado,_ = quantificacao(sinal,T[0],T[1])
    print sinal_quantificado
    #print sinal_quantificado
    #des_quant = quantificacao_inversa(T[0],sinal_quantificado)
    #print des_quant
#    plt.subplot(212)
#    plt.ylabel('Amplitude')
#    plt.xlabel('Tempo')
#    plt.title('Amostras do Sinal Quantificado')
#    plt.plot(t,sinal_quantificado, "o")
#    plt.show()
#    plt.figure(1)
#
#
############################## Exercicio 3b) ##################################
#    A = 20006.0
#    T = tabelas(A,3)
#    t = np.arange(0.,1.,Ts)
#    xq,_ = quantificacao(sinal, T[0], T[1])
#    erro = sinal - xq
#    plt.subplot(211)
#    plt.xlabel('Tempo')
#    plt.ylabel('Diferenca de Amplitudes')
#    plt.title('Erro de Quantificacao')
#    plt.plot(t,erro)
#    pylab.ylim([-3000,3000])
#    plt.subplot(212)
#    plt.xlabel('Diferenca de Amplitudes')
#    plt.ylabel('Frequencia de Acontecimento')
#    plt.title('Histograma Erro de Quantificacao')
#    plt.hist(erro)
#    plt.show()
#    pylab.xlim([-20000,20000])
#    pylab.ylim([0,800])
#    plt.figure(1)
#
#
############################## Exercicio 3c) ##################################
#    R = np.arange(3.,9.,1.)
# 
#    for x in range(len(R)):
#        Snr = SNR(A,R[x],sinal)
#          
#
############################## Exercicio 4a) ##################################
#    fs, data = wav.read('gravacao.wav')
#    plt.xlabel('Diferenca de Amplitudes')
#    plt.ylabel('Frequencia de Acontecimento')
#    plt.title('Histograma do Sinal de Audio')
#    plt.hist(data,200)
#    plt.figure(1)  
#
#
############################## Exercicio 4b) ##################################
#    
#    amostra_anterior = np.zeros(len(data))
#    
#    for i in range(len(data)):
#        anterior = i - 1
#        if i == 0:
#            anterior = 0
#        amostra_anterior[anterior] = data[i]
#        
#    plt.xlabel('Amostra Anterior')
#    plt.ylabel('Amostra Actual')
#    plt.title('Amostra do Sinal em funcao da Amostra Anterior') 
#    plt.plot(amostra_anterior,data, "*")
#
#
############################## Exercicio 4c) ##################################
#    z = max(data)
#    pot_sinal = (np.sum(1.*data**2.0))/(len(data))
#    pot = (3.0*pot_sinal)/(z**2.)
#    
#    R = np.arange(3.,9.,1.)
#    SNR_teorico = np.zeros(len(R))
#    SNR_pratico = np.zeros(len(R))
#    
#    for x in range(len(R)):
#        T = tabelas(z,R[x])
#        quant_geral,_ = quantificacao(data, T[0], T[1])
##        gravar("Som Sinal Quantificado para R = " + str(int(R[x])) + ".wav",fs,quant_geral)
#        erro = 1.*data - quant_geral
#        pot_erro = (np.sum(1.*erro**2.)/len(erro))
#        SNR_teorico[x] = (6*R[x])+10*np.log10(pot)
#        SNR_pratico[x] = 10.0 * np.log10((pot_sinal)/(pot_erro))   
#    print "SNR Teórica = ", SNR_teorico 
#    print "SNR Prático = ", SNR_pratico
#    
#    plt.figure(1)    
#    plt.xlabel('SNR Teorico em funcao de R')
#    plt.ylabel('SNR Teorico')
#    plt.title('SNR Teorico')
#    plt.plot(R,SNR_teorico)
#    pylab.ylim([10,50])
#    plt.figure(2)  
#    plt.xlabel('SNR Pratico em funcao de R')
#    plt.ylabel('SNR Pratico')
#    plt.title('SNR Pratico')
#    plt.plot(R,SNR_pratico)
    
    print(" ")    
    print("Fim do main")
    
