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

start_time = time.time()

caminho = str(sys.path[0])+"\\"
#exercicio um codigo de hamming
# c = m x G

#matriz geradora dos bits de paridade - G
#mensagem extraida da Codificacao - M

# sendo C os bits de controlo de erros a adicionar à mensagem

#numero bits de informacao
messageBits = 4
#numero bits totais
totalBits = 7
#numero bits de controlo
controlBits = totalBits-messageBits
#polinomio gerador
P = np.array([[0,1,1],[1,1,0],[1,0,1],[1,1,1]])

#mensagem de teste
teste = np.array([1,0,1,0,1])

def hamming(message):
    #tornar mensagem global na funcao
    currentMessage = message
    #verificacao do tamanho da mensagem
    resto = len(currentMessage)%messageBits
    #extenca do array inicializada
    if(not (resto == 0)):
        finalSize = len(currentMessage)+(messageBits-resto)
        currentMessage = np.zeros(finalSize)
        #preenchimento binario correto
        for i in range(len(message)):
            currentMessage[i] = message[i]

    #matriz identidade
    identity = np.eye(messageBits)
    #matriz geradora
    G = np.hstack((identity,P))
    #array de bits final
    size = len(currentMessage)+((len(currentMessage)/messageBits)*controlBits)
    finalBits = np.zeros(int(size))
    count = 0
    for i in range(0,len(currentMessage),messageBits):
        currentSlice = currentMessage[i:i+messageBits]
        #bits de paridade resultantes
        addControl =  np.mod(np.dot(currentSlice,G),2)
        for x in range(0,len(addControl)):
            finalBits[count] = addControl[x]
            count += 1

    return finalBits.astype('int16')

def sindrome(message):
    #possiveis sindromas
    sindromeTable = np.array([[0,1,1],[1,1,0],[1,0,1],[1,1,1],[1,0,0],[0,1,0],[0,0,1]])
    #percorre o sinal
    for i in range(0, len(message), totalBits):
        currentMessage = message[i:i+totalBits]
        #resultado do sindroma multiplicado por matriz de teste de paridade
        sindromeResult = np.mod(np.dot(currentMessage,sindromeTable),2)
        size = (len(message)/totalBits)*messageBits
        correctedMessage = np.zeros(int(size))
        index = 0
        count = 0
        errors = 0
        for x in range(0,len(sindromeTable)):
            if(sum(sindromeTable[x]==sindromeResult)==controlBits):
                message[i+count] = (message[i+count]+1)%2
                #apenas corrige um erro
                break
            else:
                count+=1
        if(sum(sindromeResult)!=0):
            errors += 1
        count =0
        correctedMessage[index:index+messageBits] = message[i:i+messageBits]
        index += messageBits

    return errors, correctedMessage.astype('int16')

def simulation():

    fsRecord, data = wav.read(caminho+"sinaldevoz8khz.wav")
    R = 8
    BERt = 0.1

    VD,NQ = createTable(R,np.max(np.abs(data)))
    SQ, IQ = quantificacao(data,NQ,VD)
    signalCodif = codificaSinal(IQ,R)
    signalControl = hamming(signalCodif)

    print( "CODIGO HAMMING RETURN : " + str(signalControl))
    print("\n")
    whiteNoise = 1*np.logical_xor(signalControl, np.random.binomial(1,BERt, len(signalControl)))

    print("white noise signal: " + str(whiteNoise))
    print("\n")
    errors, corrected = sindrome(whiteNoise)

    BerScorrecao = sum((signalControl + whiteNoise)%2.)/float(len(signalControl))
    print ("BER sem correcao")
    print (str(BerScorrecao))
    print("\n")

    berCcorrecao = float(errors)/float(len(signalCodif))
    print ("BER com correcao")
    print (str(berCcorrecao))

    print(corrected)

    decodedSignal = descodificaSinal(corrected,R)

    signalQuant = quantificacaoInversa(decodedSignal,NQ)

    print(signalQuant)
    print(data)

    recordSignal("novoSinal.wav",fsRecord,signalQuant)



if __name__ == "__main__":
    # mensagem = np.array([1,0,0,0,0])
    #
    # mensagemControl = hamming(mensagem)
    #
    # print(mensagemControl)

    simulation()
