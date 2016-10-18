# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
import sys
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
    plt.title('Espectro do sinal')
    plt.xlabel('Frequencia')
    plt.ylabel('Amplitude')

def recordSignal(name, freq, signal):
    wav.write(caminho+name,freq,signal.astype('int16'))

def EX1A():
    figure = plt.figure()
    #SINAL NORMAL
    tnormal, ynormal = samplingSignal(A,0.,1.,ts)
    #5 PERIODOS DO SINAL
    t5p, signal = samplingSignal(A,0.,5.*1/f,ts)
    figure.add_subplot(211)
    plt.plot(t5p,signal)
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.title('Sinusoide gerada - Amostragem 5 periodos - 8khz')
    figure.add_subplot(212)
    spectrumSignal(fs,ynormal)
    plt.show()
    figure.savefig(caminho+'EX1A.png')

    recordSignal('sinal8khz.wav',fs,ynormal.astype('int16'))

def EX1B():
    newData = data[:fs]
    figure = plt.figure()
    tRecord = np.arange(0.,1.,1./fsRecord)
    figure.add_subplot(211)
    plt.plot(tRecord,data[:fs])
    # print("Tamanho do array data: " + str(len(newData)))
    # print("Tamanho do array tempo: " + str(len(tRecord)))
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.title('Sinal gravado')
    figure.add_subplot(212)
    spectrumSignal(fsRecord,newData)
    plt.show()
    figure.savefig(caminho+'EX1B.png')

def EX2A():
    newFs = 4000
    newTs = 1./newFs

    figure = plt.figure()

    newT, newSignal = samplingSignal(A,0.,1.,newTs)

    plt.plot(newT, newSignal)
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.title('Sinusoide a 4khz')
    plt.show()
    figure.savefig(caminho+'EX2A.png')

    recordSignal('sinal4khz.wav',newFs, newSignal.astype('int16'))

#em comparacao com o primeiro sinal podemos reparar no grafico
#que tem menos amostras, e que ouvindo o sinal notamos frequencias
#mais baixas emitindo sons mais graves

def EX2B():
    newFs = 1000
    newData = data[::8]
    figure = plt.figure()
    recordSignal('sinaldevoz1khz.wav',newFs,newData.astype('int16'))
    figure.add_subplot(211)
    spectrumSignal(newFs, newData[:newFs])
    figure.add_subplot(212)
    spectrumSignal(fs, data[:fs])
    plt.show()
    figure.savefig(caminho + 'EX2B.png')





if __name__ == "__main__":
    # EX1A()
    # EX1B()
    # EX2A()
    EX2B()
