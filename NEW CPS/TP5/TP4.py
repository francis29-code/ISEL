# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
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

def codigoPRZ(arrayBits,P,A):
    #sinal codificado, numero de amostras por bit, amplitude do codigo
    arrayPRZ = np.zeros(len(arrayBits)*P)
    aux = int(P/2)
    for i in range(len(arrayBits)):
        current = arrayPRZ[i*P:(i+1)*P]
        if(arrayBits[i]==0):
            current[:aux] = -A
            current[aux:] = 0
        else:
            current[:aux] = A
            current[aux:] = 0

    return arrayPRZ.astype("int16")


def adaptiveFilter(codLinha, lim, P):
    filtered = np.zeros(int(len(codLinha)/P))
    #vetor base
    c = np.ones(P)*(1/np.sqrt(P))
    aux = int(P/2)
    c[aux:]*=-1
    for i in range(len(filtered)):
        value = sum(c*codLinha[i*P:(i+1)*P])
        if(value > lim):
            filtered[i]=1
        else:
            filtered[i]=0

    return filtered.astype("int16")

def canalAWGN(signal,noisePower):
    signalOut = signal + np.sqrt(noisePower)*np.random.randn(len(signal))
    return signalOut

def BERteorico(arrayIN, arrayOUT):
    BerScorrecao = sum(1*np.logical_xor(arrayIN,arrayOUT))/float(len(arrayOUT))
    berTeorico = ((3.0*6.0)/2.0)*(BerScorrecao**2.0)
    return berTeorico

def BERpratico(arrayIN,arrayOUT):
    erro=0
    for i in range(len(arrayIN)):
        if(arrayIN[i] != arrayOUT[i]):
            erro = erro +1

    return float(erro)/float(len(arrayIN))

def EX4A():
    bits = [0,1,1,0,0,1]
    P = 8
    A = 1
    Pr = 1
    lim = 0

    codePRZ = codigoPRZ(bits,P,A)
    canal = canalAWGN(codePRZ,Pr)
    filtrado = adaptiveFilter(canal,lim,P)

    figure = plt.figure()
    plt.plot(bits)
    plt.plot(filtrado)
    figure.savefig(caminho+"ex4a.png")
    plt.show()

    print("array inicial: " + str(bits))
    print("\n")
    print("array PRZ: " + str(codePRZ))
    print("\n")
    print("array Canal: " + str(canal))
    print("\n")
    print("array Filtrado: " + str(filtrado))

def EX4B():

    bits = [0,1,1,0,0,1]
    P = 8
    A = 1
    Pr = [0.5,1,2]
    lim = 0
    plots = []

    for i in range(len(Pr)):
        codePRZ = codigoPRZ(bits,P,A)
        canal = canalAWGN(codePRZ,Pr[i])
        filtrado = adaptiveFilter(canal,lim,P)

        print("PARA A POTENCIA DE RUIDO: " + str(Pr[i]))
        print("\n")
        print("array inicial: " + str(bits))
        print("\n")
        print("array PRZ: " + str(codePRZ))
        print("\n")
        print("array Canal: " + str(canal))
        print("\n")
        print("array Filtrado: " + str(filtrado))
        print("\n")
        plots.append(filtrado)

    fig,axs = plt.subplots(3,1)
    axs[0].plot(plots[0])
    axs[0].plot(bits)
    axs[1].plot(plots[1])
    axs[1].plot(bits)
    axs[2].plot(plots[2])
    axs[2].plot(bits)
    fig.savefig(caminho + "Potencias.png")
    plt.show()

def EX5():
    P = 8
    A = 1
    Pr = [0.5,1,2,4]
    lim = 0
    berTeorico = np.zeros(len(Pr))
    berPratico = np.zeros(len(Pr))
    snrPratica = np.zeros(len(Pr))

    fsRecord, data = wav.read(caminho+"sinaldevoz8khz.wav")
    R = 8
    for i in range(len(Pr)):
        #criacao das tabelas
        VD,NQ = createTable(R,np.max(np.abs(data)))
        #quantificacao do sinal lido
        SQ, IQ = quantificacao(data,NQ,VD)
        #codificacao do sinal quantificado
        signalCodif = codificaSinal(IQ,R)
        #adicao dos bits de erro
        signalControl = hamming(signalCodif)
        #gerar o codigoPRZ
        PRZ = codigoPRZ(signalControl,P,A)
        #passagem pelo canal
        canal = canalAWGN(PRZ,Pr[i])
        #aplicação do filtro
        filtrado = adaptiveFilter(canal,lim,P)
        #correcao hamming
        correctedB, corrected = sindrome(filtrado)
        #descodificacao do sinal
        decodedSignal = descodificaSinal(corrected,R)
        #desquantificacao do sinal
        signalQuant = quantificacaoInversa(decodedSignal,NQ)
        ################ ---- ERROS ------ ##########################
        ####----------medicao de BER's------------####
        berTeorico[i] = BERteorico(signalControl,filtrado)
        berPratico[i] = BERpratico(signalCodif,corrected)
        # berPratico[i] = correctedB/len(signalCodif)

        ## medicao da SNRPratica
        erro = erroQuantificacao(data,signalQuant)
        potenciaErro = potenciaErroQuant(erro)
        potencia = potenciaSinal(data)
        snrPratica[i] = SNRPratico(potencia,potenciaErro)

    print("array ber teoricos: " + str(berTeorico))
    print("\n")
    print("array ber pratico: " + str(berPratico))
    print("\n")
    print("array SNR Pratica: " + str(snrPratica))
    print("\n")





if __name__ == "__main__":
    # EX4A()
    EX4B()
    # EX5()

print("--- %s seconds ---" % (time.time() - start_time))
