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
from TP3 import hamming, sindrome
from TP4 import BERteorico, BERpratico

start_time = time.time()

caminho = str(sys.path[0])+"\\"

teste = np.array([0,0,1,1,0,1,1,0])

#dicionario das fases correspondentes aos bits transmitidos do codigo de HAMMING
fases = {"11":np.pi/4,"01":3*np.pi/4,"00":5*np.pi/4,"10":7*np.pi/4}


def QPSK(arrayBits,P,Eb):
    #sabemos que é uma modelação com 4 simbolos
    #logo assumimos que a cada simbolo agrupamos 2 bits
    nBits = 2
    ##########
    currentMessage = arrayBits
    #verificacao do tamanho da mensagem
    resto = len(currentMessage)%nBits
    #extenca do array inicializada
    if(not (resto == 0)):
        finalSize = len(currentMessage)+(messageBits-resto)
        currentMessage = np.zeros(finalSize)
        #preenchimento binario correto
        for i in range(len(arrayBits)):
            currentMessage[i] = arrayBits[i]

    #iterador do array de fases
    currentPosition = 0
    #calculo da amplitude constante
    #quanto maior a energia de BIT maiores as amplitudes no canal,
    #maior a potencia do sinal
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
            # calculoX = A*np.cos(arrayFases[i])+np.cos(((2*np.pi*j)/P))
            # calculoY = -A*np.sin(arrayFases[i])+np.sin(((2*np.pi*j)/P))
            # calculo = calculoX+calculoY
            secondArray[aux] = calculo
            aux += 1

    #calculos para representação da constelação
    valoresConstelacaoX = np.zeros(int((len(secondArray)/P)*2))
    valoresConstelacaoY = np.zeros(int((len(secondArray)/P)*2))
    Rs = 1/P
    arrayQPSKdesmodulado = np.zeros(int((len(secondArray)/P)*2))
    finalArrayX = np.zeros(P)
    finalArrayY = np.zeros(P)
    for i in range(int(len(arrayQPSKdesmodulado)/2)):
        current = secondArray[i*P:(i+1)*P]
        for j in range(0,P):
            calculoY = -np.sqrt(2*Rs)*np.sin((2*np.pi*j)/P)*current[j]
            calculoX = np.sqrt(2*Rs)*np.cos((2*np.pi*j)/P)*current[j]
            # plt.plot(calculoX,calculoY,'o')
            finalArrayY[j] = calculoY
            finalArrayX[j] = calculoX

        #somatorio do array
        valueY = sum(finalArrayY)
        valueX = sum(finalArrayX)
        valoresConstelacaoY[i] = valueY
        valoresConstelacaoX[i] = valueX

        finalArrayX = np.zeros(P)
        finalArrayY = np.zeros(P)

    return secondArray,valoresConstelacaoX,valoresConstelacaoY


def desmodulacao(arrayQPSK,P):
    #ritmo de simbolos
    Rs = 1/P
    valueX = 0
    valueY = 0
    valoresConstelacaoX = np.zeros(int((len(arrayQPSK)/P)*2))
    valoresConstelacaoY = np.zeros(int((len(arrayQPSK)/P)*2))
    finalArrayX = np.zeros(P)
    finalArrayY = np.zeros(P)

    arrayQPSKdesmodulado = np.zeros(int((len(arrayQPSK)/P)*2))

    for i in range(int(len(arrayQPSKdesmodulado)/2)):
        current = arrayQPSK[i*P:(i+1)*P]
        for j in range(0,P):
            #multiplicação pelo vetor base
            calculoY = -np.sqrt(2*Rs)*np.sin((2*np.pi*j)/P)*current[j]
            calculoX = np.sqrt(2*Rs)*np.cos((2*np.pi*j)/P)*current[j]
            # plt.plot(calculoX,calculoY,'o')
            finalArrayY[j] = calculoY
            finalArrayX[j] = calculoX

        #simulação da integração no tempo
        #somatorio das amostras em tempo discreto
        valueY = sum(finalArrayY)
        valueX = sum(finalArrayX)

        valoresConstelacaoY[i] = valueY
        valoresConstelacaoX[i] = valueX

        #construção do array final
        if(valueX > 0):
            arrayQPSKdesmodulado[i*2] = 1
        else:
            arrayQPSKdesmodulado[i*2] = 0

        if(valueY > 0):
            arrayQPSKdesmodulado[(i*2)+1] = 1
        else:
            arrayQPSKdesmodulado[(i*2)+1] = 0

        ##reset aos arrays para não iterar
        finalArrayX = np.zeros(P)
        finalArrayY = np.zeros(P)


    return arrayQPSKdesmodulado.astype("int16"), valoresConstelacaoX, valoresConstelacaoY


def constelation(x,y,when,potencia,Eb):
    if(when == "Antes"):
        plt.title("Constelação "+str(when) + " do canalAWGN - Eb "+str(Eb))
    else:
        plt.title("Constelação "+str(when) + " do canalAWGN - Potencia Ruido "+str(potencia) + " - Eb "+str(Eb))
    plt.plot(x,y,'o')
    plt.grid(True)
    plt.show()


def canalAWGN(signal,noisePower):
    signalOut = signal + np.sqrt(noisePower)*np.random.randn(len(signal))
    return signalOut


def sistema(correcao):
    #parametos correcao indica se queremos o sistema com controlo de erros ou não
    P = 8
    Eb = 1
    Pr = [0.5,1,2,4]
    berTeoricoBefore = np.zeros(len(Pr))
    berPraticoBefore = np.zeros(len(Pr))
    snrPratica = np.zeros(len(Pr))
    berTeoricoAfter = np.zeros(len(Pr))
    berPraticoAfter = np.zeros(len(Pr))
    fsRecord, data = wav.read(caminho+"sinaldevoz8khz.wav")
    R = 8
    for i in range(len(Pr)):
        #criacao das tabelas
        VD,NQ = createTable(R,np.max(np.abs(data)))
        #quantificacao do sinal lido
        SQ, IQ = quantificacao(data,NQ,VD)
        #codificacao do sinal quantificado
        signalCodif = codificaSinal(IQ,R)

        if(correcao):
            #adicao dos bits de erro
            signalControl = hamming(signalCodif)
            #gerar o QPSK
            sinalQPSK,x1,y1 = QPSK(signalControl,P,Eb)
        else:
            #gerar o QPSK
            sinalQPSK,x1,y1 = QPSK(signalCodif,P,Eb)
        #constelação antes do canal
        constelation(x1,y1,"Antes",Pr[i],Eb)
        #passagem pelo canal
        canal = canalAWGN(sinalQPSK,Pr[i])
        #aplicação da desmodulacao
        desmodulado,x2,y2 = desmodulacao(canal,P)
        #constelação depois do canal
        constelation(x2,y2,"Depois",Pr[i],Eb)

        if(correcao):
            #correcao hamming
            correctedB, corrected = sindrome(desmodulado)
            #descodificacao do sinal
            decodedSignal = descodificaSinal(corrected,R)
        else:
            #descodificacao do sinal
            decodedSignal = descodificaSinal(desmodulado,R)
        #desquantificacao do sinal
        signalQuant = quantificacaoInversa(decodedSignal,NQ)

        ################## ---- ERROS ------ ########################
        ######-------------medicao de BER's----------------------####
        if(correcao):
            berTeoricoBefore[i] = BERteorico(signalCodif,corrected)
            berPraticoBefore[i] = BERpratico(signalCodif,corrected)

            berTeoricoAfter[i] = 0.5*erfc(np.sqrt(Eb/Pr[i]))
            berPraticoAfter[i] = np.sum(1*np.logical_xor(signalControl,desmodulado))/len(desmodulado)
        else:
            berTeoricoAfter[i] = 0.5*erfc(np.sqrt(Eb/Pr[i]))
            berPraticoAfter[i] = np.sum(1*np.logical_xor(signalCodif,desmodulado))/len(desmodulado)

        ## medicao da SNRPratica
        erro = erroQuantificacao(data,signalQuant)
        potenciaErro = potenciaErroQuant(erro)
        potencia = potenciaSinal(data)
        snrPratica[i] = SNRPratico(potencia,potenciaErro)

        if(correcao):
            recordSignal("sinal-ruido-"+str(Pr[i])+"-Ccorrecao.wav",fsRecord,signalQuant.astype('int16'))
        else:
            recordSignal("sinal-ruido-"+str(Pr[i])+"-Scorrecao.wav",fsRecord,signalQuant.astype('int16'))

    plt.figure()
    if(correcao):
        plt.title("BER teorico e Pratico Depois Hamming Ccorrecao")
    else:
        plt.title("BER teorico e Pratico Scorrecao")
    plt.plot(Pr,berTeoricoAfter,'r',label='BERteorico')
    plt.plot(Pr,berPraticoAfter,'b',label='BERpratico')
    plt.ylabel('valores de BER')
    plt.xlabel('valores de Potencia de Ruido')
    plt.legend(loc='upper left')
    plt.grid(True)
    if(correcao):
        plt.savefig(caminho + 'depoishamming-Ccorrecao.png')
    else:
        plt.savefig(caminho + 'BER-Scorrecao.png')

    if(correcao):
        plt.figure()
        plt.title("BER teorico e Pratico Antes Hamming")
        plt.plot(Pr,berTeoricoBefore,'r',label='BERteorico')
        plt.plot(Pr,berPraticoBefore,'b',label='BERpratico')
        plt.legend(loc='upper left')
        plt.ylabel('valores de BER')
        plt.xlabel('valores de Potencia de Ruido')
        plt.savefig(caminho + 'anteshamming Ccorrecao.png')
        plt.grid(True)

    plt.figure()
    if(correcao):
        plt.title("SNR Pratica do sinal Ccorrecao")
    else:
        plt.title("SNR Pratica do sinal Scorrecao")
    plt.plot(Pr,snrPratica,'r',label='SNR Pratica')
    plt.legend(loc='upper right')
    plt.ylabel('valores de SNR')
    plt.xlabel('valores de Potencia de Ruido')
    if(correcao):
        plt.savefig(caminho + 'SNR-Ccorrecao.png')
    else:
        plt.savefig(caminho + 'SNR-Scorrecao.png')
    plt.grid(True)
    plt.show()




if __name__ == "__main__":
    sistema(False)
    # simulate_teste()
