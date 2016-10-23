# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
import sys
import pylab as pyl
# from soundPlay import soundPlay
# print ("caminho absoluto: " + str(sys.path[0]))
#caminho estático de gravações
caminho = str(sys.path[0])+"\\"

#variaveis constantes
f = 3014.0
A = 20000
fs = 8000
ts = 1./fs

#leitura do sinal gravado
fsRecord, data = wav.read(caminho + 'novosom.wav')

def samplingSignal(amp, start, stop, step):
    #função retorna o array correspondente ao periodo e
    #a expressão da sinusoide
    #array correspondente ao periodo
    t=np.arange(start,stop,step)
    #sinusoide
    y = amp*np.cos(2*np.pi*f*t)
    return(t, y)

def spectrumSignal(freqS, sin):
    #aplica-se a transformada de fourier
    sinusoideFFT = np.fft.fft(sin)
    #shift recalcula os valores da frequencias
    shiftedFFT = np.fft.fftshift(sinusoideFFT)
    t = np.arange(-freqS/2,freqS/2)
    plt.plot(t,shiftedFFT)
    plt.title("Espectro do sinal a " + str(freqS) + " hz")
    plt.xlabel('Frequencia')
    plt.ylabel('Amplitude')

def recordSignal(name, freq, signal):
    wav.write(caminho+name,freq,signal.astype('int16'))

def EX1A():
    #SINAL NORMAL
    tnormal, ynormal = samplingSignal(A,0.,1.,ts)
    plt.plot(tnormal,ynormal)
    plt.title('Sinusoide gerada - Amostrada Fs = 8khz')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    figure = plt.figure()
    #5 PERIODOS DO SINAL
    t5p, signal = samplingSignal(A,0.,5.*1/f,ts)
    figure.add_subplot(211)
    #grafico dos 5 periodos da sinusoide
    plt.plot(t5p,signal)
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.title('Sinusoide gerada - Amostragem 5 periodos - 8khz')
    figure.add_subplot(212)
    #espectro do sinal normal
    spectrumSignal(fs,ynormal)

    plt.show()
    figure.savefig(caminho+'EX1A.png')

    recordSignal('sinal8khz.wav',fs,ynormal)

def EX1B():
    #sinal de voz gravdo
    newData = data[:fs]
    figure = plt.figure()
    tRecord = np.arange(0.,1.,1./fsRecord)
    figure.add_subplot(211)
    #grafico do sinal de voz gravado a 8khz
    plt.plot(tRecord,data[:fs])
    # print("Tamanho do array data: " + str(len(newData)))
    # print("Tamanho do array tempo: " + str(len(tRecord)))
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.title('Sinal gravado')
    figure.add_subplot(212)
    #espectro do sinal gravado
    spectrumSignal(fsRecord,newData)
    plt.show()
    figure.savefig(caminho+'EX1B.png')

def EX2A():
    newFs = 4000
    newTs = 1./newFs

    figure = plt.figure()
    #sinusoide amostrada a uma frequencia de 4khz
    newT, newSignal = samplingSignal(A,0.,1.,newTs)
    #grafico da sinusoide a 4khz
    plt.plot(newT, newSignal)
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.title('Sinusoide a 4khz')
    plt.show()
    figure.savefig(caminho+'EX2A.png')

    recordSignal('sinal4khz.wav',newFs, newSignal)

#em comparacao com o primeiro sinal podemos reparar no grafico
#que tem menos amostras, e que ouvindo o sinal notamos frequencias
#mais baixas emitindo sons mais graves

def EX2B():
    newFs = 1000
    #se queremos extrair apenas 1000 amostras num segundo
    #dividimos a frequencia de amostragem do sinal pela frequencias
    #de amostragem que queremos reconstruir o sinal
    newData = data[:fsRecord]
    newData1 = data[::fsRecord/newFs]
    #arra de data com tamanho igual amostragem
    newData_1k = newData1[:newFs]
    #array de tempo igual a amostragem
    newT = np.arange(0.,1.,1./newFs)
    #grafico do sinal de voz amostrado a uma frequencia de 1khz
    plt.plot(newT,newData_1k)
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.title('Amostragem o sinal de voz com FS=1KHZ')
    recordSignal('sinaldevoz1khz.wav',newFs,newData_1k)
    figure = plt.figure()
    figure.add_subplot(211)
    #espectro do sinal de voz amostrado a 1khz
    spectrumSignal(newFs, newData_1k)
    figure.add_subplot(212)
    #espectro do sinal de voz amostrado a 8khz
    spectrumSignal(fsRecord, data[:fsRecord])
    plt.show()
    figure.savefig(caminho + 'EX2B.png')


if __name__ == "__main__":
    EX1A()
    EX1B()
    EX2A()
    EX2B()
