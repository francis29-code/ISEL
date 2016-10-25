# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:37:34 2015

@author: Hugo Safara
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import pylab as pylab
plt.close('all')

f = 3014.0
A = 20000
Fs = 8000.0                                     #frequencia de amostragem
Ts = 1./Fs                          

fs,data = wav.read('gravacao.wav')

def amostragem(amp,inicio,fim,passo):           #função que permite gerar a amostragem da sinusóide e/ou gravação de voz
    t = np.arange(inicio,fim,passo)
    return (t,amp*np.cos(2*np.pi*f*t))
    
t,sinal = amostragem(A,0.0,1.0,Ts)              #sinusóide
    
def espectro(Fs, sin):                          #função que permite gerar o espectro da sinusóide e/ou gravação de voz
    sinusoide_fft = np.fft.fft(sin)             #é aplicada a transformada de fourier
    X = np.fft.fftshift(abs(sinusoide_fft))          #é aplicado um shitf a essa transformada para corrigir o posicionamento
    f = np.linspace(-Fs/2, Fs/2, len(sinusoide_fft))        #de -Fs/2 a Fs/2, todos os valores da janela de x, vão estar igualmente espaçados por len(X)
    plt.plot(f,X)
    plt.title('Espectro do Sinal')
    plt.xlabel('Frequencia')
    plt.ylabel('Amplitude')
    
def gravar(nome, frq, sinal):                   #função que permite gravar um sinal para wav
    wav.write(nome,frq,sinal.astype('int16'))

#Exercício 1a)
def exercicio1a():
    t_1,sinal_1 = amostragem(A,0,5.*1/f,Ts)     #amostragem do sinal em 5 periodos (5*a frequencia original do sinal, com um passo do periodo de amostragem)
    plt.subplot(211)
    plt.plot(t_1,sinal_1)
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.title('Amostragem do Sinal em 5 periodos de tempo')
    plt.subplot(212)
    espectro(Fs,sinal)    
    plt.show()
    pylab.xlim([-4000,4000])                    #Zoom em x
    pylab.ylim([0,20000])
    
    gravar("sinusoide_1.wav",Fs,sinal)
    
#Exercício 1b)
def exercicio1b():
    
    t2 = np.arange(0., 1., 1.0/fs)              #queremos representar o sinal de voz com um segundo, apesar de o sinal original ter 1.2 segundos
    plt.subplot(211)
    plt.plot(t2,data[:fs])
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.title('Amostragem do Sinal de voz')
    plt.subplot(212)
    espectro(fs,data)
    plt.show()
    pylab.xlim([-4000,4000])                    #Zoom em x
    #pylab.ylim([0,20000])  
    print data

#Exercício 2a)
def exercicio2a():  
    Fs_amo = 4000.0                             #frequência de amostragem de 4kHz
    Ts2 = 1./Fs_amo
    
    t_2,sinal_2 = amostragem(A,0.,1.,Ts2)       #representação do sinal com uma fs de 4kHz
    plt.subplot(211)
    plt.plot(t_2,sinal_2)
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.title('Amostragem do Sinal com uma frequencia fs=4kHz')
    plt.subplot(212)
    espectro(Fs_amo,sinal_2)    
    plt.show()
    pylab.xlim([-4000,4000])                    #Zoom em x
    pylab.ylim([0,10000])  
    
    gravar("sinusoide_2.wav",Fs_amo,sinal_2)

#Exercício 2b)
def exercicio2b():                              #amostragem do sinal de voz com fs = 1kHz
    freqs = 1000.0
                                                
    y = data[::fs/freqs]                        #irão se recolher 44 amostras por cada período de tempo (porque fs=44100 e freqs=1000)
    t_3 = np.arange(0.,len(y),1)                #configuraçao do x na representação do sinal
    plt.subplot(211)
    plt.plot(t_3,y)
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.title('Amostragem do Sinal de voz com a fs=1kHz')
    plt.show()
    plt.subplot(212)
    espectro(freqs,y)
    plt.show()
    pylab.ylim([0,0.14e+7])                     #Zoom em x
    pylab.xlim([-600,600])                      #Zoom em y
    
    gravar('gravacao_3.wav',freqs,y)
    
#exercicio1b()
