# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
import sys
import pylab as pylab

caminho = str(sys.path[0])+"\\"

#-------------------Funções-------------------
#calcula a potencia do sinal amostrado
def potenciaSinal(sinalAmostrado):
    potencia = (1./len(sinalAmostrado))*np.sum(sinalAmostrado**2.)
    return potencia

#calcula a potencia do sinal de erro de quantificação
def potenciaErroQuant(erroQuantificado):
    potenciaErro = (1./len(erroQuantificado))*np.sum(erroQuantificado**2.)
    return potenciaErro

#calcula o SNR teorico
def SNRTeorico(potencia,R,Vmax):
    valor = 6*R + 10*np.log((3*potencia)/Vmax**2)
    return valor

#calcula o SNR pratico
def SNRPratico(potenciaSinal, potenciaErro):
    valor = 10*np.log(potenciaSinal/potenciaErro)
    return valor

#retorna um numpy array com o erro do sinal
def erroQuantificacao(sinalOriginal, sinalQuantificado):
    erroSinal = sinalOriginal - sinalQuantificado
    return erroSinal

#retorna dois numpy arrays com os valores de
#decisão e com os niveis de quantificação
def createTable(R, Vmax):
    valoresDecisao = np.arange(-Vmax , Vmax+((2.*Vmax)/(2.**R)) , (2.*Vmax)/(2.**R))
    niveisQuantificacao = np.arange(-Vmax+(Vmax/(2.**R)) , Vmax , (2.*Vmax)/(2.**R))
    return valoresDecisao, niveisQuantificacao

#retorna dois numpy arrays com o sinal quantificado
#e outro com os indices dos niveis de quantificação usados
def quantificacao(sinalAmostrado, NQ, VD):
    sinalQuantificado = np.zeros(len(sinalAmostrado))
    indiceQuant = np.zeros(len(sinalAmostrado))
    for a in range(len(sinalAmostrado)):
        indice = sinalAmostrado[a] <= VD
        indiceTrue = np.nonzero(indice)
        aux = int(indiceTrue[0][0]-1)
        indiceQuant[a] = aux
        sinalQuantificado[a] = NQ[aux]
    return sinalQuantificado , indiceQuant.astype('int16')

#Codifica em binario o array de Indices
#retorna um numpy array com os valores em binario a 3 bit
#os valores do array de indices
def codificaSinal(IQ, R):
    sinalCodificado = np.zeros(len(IQ)*R)
    count=0
    binario = '{0:0'+str(R)+'b}'
    for i in range(len(IQ)):
        aux = binario.format(IQ[i])
        sinalCodificado[count]=aux[0]
        sinalCodificado[count+1]=aux[1]
        sinalCodificado[count+2]=aux[2]
        count+=3
    return sinalCodificado.astype('int16')



def recordSignal(name, freq, signal):
    wav.write(caminho+name,freq,signal.astype('int16'))

#-------------Reverse MotherFucker-------------------

def descodificaSinal(sinalCodificado, R):
    sinalDescodificado = np.zeros(len(sinalCodificado)/R)
    count = 0
    for i in range(0,len(sinalCodificado),3):
        binario = str(sinalCodificado[i])+str(sinalCodificado[i+1])+str(sinalCodificado[i+2])
        sinalDescodificado[count]=int(binario,2)
        count+=1

    return sinalDescodificado.astype('int16')

def quantificacaoInversa(sinalDescodificado,niveisQuantificacao):
    sinalQuantInv = np.zeros(len(sinalDescodificado))
    for i in range(len(sinalDescodificado)):
        sinalQuantInv[i]=niveisQuantificacao[sinalDescodificado[i]]
    return sinalQuantInv

#--------------------Variaveis-----------------------
R = 3
Vmax = 1
SinalRampa=np.arange(-1,1,0.01)
fs = 8000.
f = 3014.
T = np.arange(0,1,1/fs)
A = 1

y = A*np.cos(2*np.pi*f*T)

#--------------Execução de funções-------------------
VD,NQ = createTable(R,Vmax)
SQ,IQU = quantificacao(SinalRampa , NQ, VD)
potencia = potenciaSinal(SinalRampa)
erro = erroQuantificacao(SinalRampa,SQ)
potenciaErro = potenciaErroQuant(erro)
sinalCodificado = codificaSinal(IQU, R)
sinalDescodificado = descodificaSinal(sinalCodificado,R)
sinalQuantInv = quantificacaoInversa(sinalDescodificado,NQ)
recordSignal('sinosoide.wav',fs,SinalRampa)
recordSignal('sinalQuantificado.wav',fs,SQ)
recordSignal('sinalQuantInv.wav',fs,sinalQuantInv)


#----------------------Prints------------------------
print ("------------------------------------------------------------------------")
print ("Niveis de Quantificação: \n" + str(NQ))
print ("------------------------------------------------------------------------")
print ("Valores de Decisão: \n" + str(VD))
print ("------------------------------------------------------------------------")
print ("Potencia do sinal: " + str(potencia))
print ("------------------------------------------------------------------------")
print ("sinalQuantificado: \n" + str(SQ))
print ("------------------------------------------------------------------------")
print ("Indices de Quantificação utilizados: \n" + str(IQU))
print ("------------------------------------------------------------------------")
print ("Erro de Quantificação: \n" + str(erro))
print ("------------------------------------------------------------------------")
print ("Potencia do Erro de Quantificação: \n" + str(potenciaErro))
print ("------------------------------------------------------------------------")
print ("Codificação: \n" + str(sinalCodificado))
print ("------------------------------------------------------------------------")
print ("Descodificação: \n" + str(sinalDescodificado))
print ("------------------------------------------------------------------------")
print ("Quantificação Inversa: \n" + str(sinalQuantInv))
print ("------------------------------------------------------------------------")



#-----------------------Plots-----------------------
Tsq=np.arange(0,len(SQ))
plt.grid(True)
plt.plot(Tsq,SQ, label='SinalQuantificado')
plt.plot(Tsq,SinalRampa, label='SinalRampa')
plt.legend(loc='lower right')
plt.show()
