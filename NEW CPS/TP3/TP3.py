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
    sindromeTable = np.array([[0,0,0],[0,1,1],[1,1,0],[1,0,1],[1,1,1],[1,0,0],[0,1,0],[0,0,1]])
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
            if(sum(P[x]==sindromeResult)==controlBits):
                mensagem[i+count] = (mensagem[i+count]+1)%2
                #apenas corrige um erro
                break
            else:
                count+=1
        if(sum(sindromeResult)!=0):
            errors += 1
        count =0
        correctedMessage[count:count+messageBits] = message[i:i+messageBits]
        index += messageBits

    return errors, correctedMessage.astype('int16')

def simulation(message):

    BER = 0.1
    #erro aplica-se à mensagem codificada

    VQ,VD = CriarTabela(R,A)
    SQ, VaQ = SinalQuantificado(y,VQ,VD)
    SinalCodificado = IntparaBin(VaQ,R)

    H = Hamming(SinalCodificado)

    print "CODIGO HAMMING RETURN : " + str(H)

    SinalComRuido = 1*np.logical_xor(H, np.random.binomial(1,0.1, len(H)))

    corrigido = Sindroma(SinalComRuido)

    BerScorrecao = sum((H + SinalComRuido)%2.)/float(len(H))
    print "BER sem correcao"
    print BerScorrecao

    err=0.
    for i in range(len(SinalCodificado)):
        if(SinalCodificado[i] != corrigido[i]):
            err=err+1

    ber = float(err)/float(len(SinalCodificado))
    print "BER com correcao"
    print ber

    ##calculo do ber vê-se com
    y = 1*np.logical_xor(x,np.binomial(1,BER,len(message)))




if __name__ == "__main__":
    # sindrome()
    a = np.array([1,2,3])
    b = np.array([3,2,1])
    c = a+b
    print(c)
    # sindromeTable = np.array([[0,1,1],[1,1,0],[1,0,1],[1,1,1],[1,0,0],[0,1,0],[0,0,1]])
    # x = np.array([1,1,1,3,3,4,5,6,7,8,8,7,6,5,5,45,5,3,3,3,3])
    # print(str(len(x)))
    # size = (len(x)/7)*4
    # print(str(int(size)))
    # for i in range(len(sindromeTable)):
    #     print(str(sindromeTable[i]))
    #     if(sum(sindromeTable[i] == x) == 3):
    #         print(True)
    #         break
    # y = np.array([0,1,1,1])
    # print(sum(y))
    # x = hamming(y)
    # sindromeResult = np.mod(np.dot(x,sindromeTable),2)
    # print(x)
    # print(sindromeResult)

    # print(sindromeTable[1])
    # print(sindromeTable[4]==y)
    # print(str(sum(sindromeTable[4]==y)))


    # hamming(teste)
