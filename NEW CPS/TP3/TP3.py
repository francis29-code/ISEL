# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
import sys
import pylab as pylab
import time

start_time = time.time()

caminho = str(sys.path[0])+"\\"
#exercicio um codigo de hamming
# c = m x G

#matriz geradora dos bits de paridade - G
#mensagem extraida da Codificacao - M

# sendo C os bits de controlo de erros a adicionar à mensagem

#bits de informacao
messageBits = 4
#bits totais
totalBits = 7
#bits de paridade
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

    return finalBits

def sindrome(message):
    




    return wila


if __name__ == "__main__":

    # hamming(teste)
