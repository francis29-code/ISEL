# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
from scipy.special import erfc
import sys
import pylab as pylab
import time
from TP2e3 import createTable
from TP2e3 import quantificacao
from TP2e3 import codificaSinal
from TP2e3 import SNRTeorico
from TP2e3 import SNRPratico
from TP2e3 import potenciaErroQuant
from TP2e3 import erroQuantificacao
from TP2e3 import potenciaSinal
from TP2e3 import descodificaSinal
from TP2e3 import quantificacaoInversa
from TP2e3 import recordSignal
from TP3 import hamming
from TP3 import sindrome

start_time = time.time()

caminho = str(sys.path[0])+"\\"

teste = np.array([0,0,1,1,0,1,1,0])

#dicionario das fases correspondentes aos bits transmitidos do codigo de HAMMING
fases = {"11":np.pi/4,"01":3*np.pi/4,"00":5*np.pi/4,"10":7*np.pi/4}


def QPSK(arrayBits,P,Eb):
    #sabemos que é uma modelação com 4 intervalos
    #logo assumimos que a cada simbolo agrupamos 2 bits
    nBits = 2
    #iterador do array de fases
    currentPosition = 0
    #calculo da amplitude constante
    A = np.sqrt(Eb*4)
    #fases correspondentes aos bits
    arrayFases = np.zeros(int(len(arrayBits)/2))
    for i in range(0,len(arrayBits),nBits):
        currentBits = arrayBits[i:i+nBits]
        if(currentBits[0]==0):
            if(currentBits[1]==0):
                arrayFases[currentPosition] = fases["00"]
            else:
                arrayFases[currentPosition] = fases["01"]
        else:
            if(currentBits[1]==0):
                arrayFases[currentPosition] = fases["10"]
            else:
                arrayFases[currentPosition] = fases["11"]


        currentPosition +=1;

    secondArray = np.zeros(len(arrayFases)*P)
    aux = 0

    for i in range(len(arrayFases)):
        for j in range(0,P):
            calculo = A*np.cos(((2*np.pi*j)/P) + arrayFases[i])
            secondArray[aux] = calculo
            aux += 1

    ################## EFEITOS DE TESTE ###########################3
    # t = np.arange(0,len(secondArray))
    #
    # plt.plot(t,secondArray,'o')
    # plt.grid(True)
    # plt.show()


    ###############################################################

    return secondArray

def desmodulacao(arrayQPSK,P):
    #ritmo de simbolos
    Rs = 1/P
    valueX = 0
    valueY = 0
    finalArrayX = np.zeros(P)
    finalArrayY = np.zeros(P)

    arrayQPSKdesmodulado = np.zeros(int((len(arrayQPSK)/P)*2))

    ######################PONTOS DE REFERENCIA####################
    # plt.plot(-1,1,'o')
    # plt.plot(1,1,'o')
    # plt.plot(-1,-1,'o')
    # plt.plot(1,-1,'o')
    # plt.plot(0,0,'o')
    #############################################################
    for i in range(int(len(arrayQPSKdesmodulado)/2)):
        current = arrayQPSK[i*P:(i+1)*P]
        for j in range(0,P):
            calculoY = -np.sqrt(2*Rs)*np.sin((2*np.pi*j)/P)*current[j]
            calculoX = np.sqrt(2*Rs)*np.cos((2*np.pi*j)/P)*current[j]
            plt.plot(calculoX,calculoY,'o')
            # plt.plot(calculoY,calculoX,'o')
            finalArrayY[j] = calculoY
            finalArrayX[j] = calculoX

        valueY = sum(finalArrayY)
        valueX = sum(finalArrayX)
        # plt.plot(valueX,valueY,'o')

        ##reset aos arrays para não iterar
        finalArrayX = np.zeros(P)
        finalArrayY = np.zeros(P)

        #construção do array final
        if(valueX > 0):
            arrayQPSKdesmodulado[i*2] = 1
        else:
            arrayQPSKdesmodulado[i*2] = 0

        if(valueY > 0):
            arrayQPSKdesmodulado[(i*2)+1] = 1
        else:
            arrayQPSKdesmodulado[(i*2)+1] = 0


    plt.grid(True)
    plt.show()

    return arrayQPSKdesmodulado.astype("int16")


def canalAWGN(signal,noisePower):
    signalOut = signal + np.sqrt(noisePower)*np.random.randn(len(signal))
    return signalOut

if __name__ == "__main__":
    P=400
    R=3

    # fsRecord, data = wav.read(caminho + 'sinaldevoz8khz.wav')
    # VD,NQ = createTable(R,np.max(np.abs(data)))
    # #quantificacao do sinal lido
    # SQ, IQ = quantificacao(data,NQ,VD)
    # #codificacao do sinal quantificado
    # signalCodif = codificaSinal(IQ,R)
    # # #adicao dos bits de erro
    # signalControl = hamming(signalCodif)
    #####################
    array = QPSK(teste,P,1)
    arrayCanal = canalAWGN(array,0.5)
    arrayD = desmodulacao(arrayCanal,P)
