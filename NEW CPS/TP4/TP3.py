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
P = np.array([[1,1,1],[1,1,0],[1,0,1],[0,1,1]])

#mensagem de teste
teste = np.array([1,0,1,0,1,1,1,1])

def hamming(message):
    # print("tamanho inicial mensagem: " + str(len(message)))
    # print("\n")
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


    # print("tamanho inicial mensagem corrigido: " + str(len(currentMessage)))
    # print("\n")
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
        # print("current slice: ")
        # print(currentSlice)
        # print("\n")
        #bits de paridade resultantes
        addControl =  np.mod(np.dot(currentSlice,G),2)
        # print("control slice: ")
        # print(addControl)
        # print("\n")
        for x in range(0,len(addControl)):
            finalBits[count] = addControl[x]
            count += 1

    return finalBits.astype('int16')

def sindrome(message):
    #possiveis sindromas
    sindromeTable = np.array([[1,1,1],[1,1,0],[1,0,1],[0,1,1],[1,0,0],[0,1,0],[0,0,1]])
    #percorre o sinal
    errors = 0
    index = 0
    count = 0
    correctedbits = 0
    size = ((len(message)/totalBits)*messageBits)
    correctedMessage = np.zeros(int(size))
    # print("tamanho da mensagme corrigida: " + str(len(correctedMessage)))
    # print("\n")
    for i in range(0, len(message), totalBits):
        currentMessage = message[i:i+totalBits]
        # print("mensagem corrente - sindroma : " + str(currentMessage))
        # resultado do sindroma multiplicado por matriz de teste de paridade
        sindromeResult = np.mod(np.dot(currentMessage,sindromeTable),2)
        # print("resultado do sindroma: " + str(sindromeResult))
        # print("\n")
        for x in range(0,len(sindromeTable)):
            if(sum(sindromeTable[x]==sindromeResult)==controlBits):
                message[i+x] = (message[i+x]+1)%2
                #apenas corrige um erro
                correctedbits += 1

                #
                # print("indice da tabela: " + str(x))
                # print("sindromeTable message: " + str(sindromeTable[x]))
                # print("numero do count: " + str(count))
                # print("\n")
                # #
                # print("entrou")
                # print("mensagem corrigida - sindroma : " + str(message[i:i+totalBits]))
                # print("\n")

                break
            else:
                count+=1
        if(sum(sindromeResult)!=0 and sum(sindromeResult)< 4):
            errors += 1
        count =0
        correctedMessage[index:index+messageBits] = message[i:i+messageBits]
        index += messageBits

    return correctedbits, correctedMessage.astype('int16')

def simulation():

    fsRecord, data = wav.read(caminho+"sinaldevoz8khz.wav")
    R = 8
    BERt = 0.1
    #criacao das tabelas
    VD,NQ = createTable(R,np.max(np.abs(data)))
    #quantificacao do sinal lido
    SQ, IQ = quantificacao(data,NQ,VD)
    #codificacao do sinal quantificado
    signalCodif = codificaSinal(IQ,R)
    #adicao dos bits de erro
    signalControl = hamming(signalCodif)
    #aplicacao de ruido
    noise = 1*np.logical_xor(signalControl, np.random.binomial(1,BERt, len(signalControl)))
    #correcao do sinal
    correctedB, corrected = sindrome(noise)
    #medicao do BER sem correcao (TEORICO)
    BerScorrecao = sum(np.logical_xor(signalControl,noise))/float(len(signalControl))
    berTeorico = ((3.0*14.0)/2.0)*(BerScorrecao**2.0)
    print("BER teorico")
    print(str(berTeorico))
    print("\n")

    #medicao do BER apos correcao
    #comparando o array inicialmente codificado com o resultante
    #da correcao
    erro=0
    for i in range(len(signalCodif)):
        if(signalCodif[i] != corrected[i]):
            erro = erro +1


    berCcorrecao = float(erro)/float(len(signalCodif))
    print ("BER com correcao (PRATICO)")
    print (str(berCcorrecao))
    print("\n")
    #descodificacao do sinal
    decodedSignal = descodificaSinal(corrected,R)
    #desquantificacao do sinal
    signalQuant = quantificacaoInversa(decodedSignal,NQ)

    ## medicao da SNRPratica
    erro = erroQuantificacao(data,signalQuant)
    potenciaErro = potenciaErroQuant(erro)
    potencia = potenciaSinal(data)
    SNRP = SNRPratico(potencia,potenciaErro)

    print("SNR Pratica do sinal")
    print(SNRP)
    print("\n")

    #gravacao do sinal apos todo o processo
    # recordSignal("sinal.wav",fsRecord,signalQuant.astype('int16'))
    wav.write(caminho+"sinal.wav",fsRecord,signalQuant.astype('int16'))



if __name__ == "__main__":
    # ber = 0.1
    simulation()

    # print("Array inicial")
    # print(teste)
    # print("\n")
    #
    #
    # testeControl = hamming(teste)
    # print("array control")
    # print(testeControl)
    # print("\n")
    # noise = 1*np.logical_xor(testeControl, np.random.binomial(1,ber, len(testeControl)))
    #
    # print("Array noise")
    # print(noise)
    # print("\n")
    #
    # bitsC, testeC = sindrome(noise)
    #
    # print("Array Corrigido")
    # print(testeC)
    # print("\n")




print("--- %s seconds ---" % (time.time() - start_time))
