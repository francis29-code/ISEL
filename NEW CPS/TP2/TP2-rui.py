import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
import sys
import pylab as plb

def potenciaSinal(sinalAmostrado):
    potencia = (1/len(sinalAmostrado))*np.sum(sinalAmostrado**2.)
    return potencia

def SNRTeorico(potencia,R):
    valor = 6*R + 10*np.log()
    return valor


def createTable(R, Vmax):
    valoresDecisao = np.arange(-Vmax , Vmax+((2.*Vmax)/(2.**R)) , (2.*Vmax)/(2.**R))
    niveisQuantificacao = np.arange(-Vmax+(Vmax/(2.**R)) , Vmax , (2.*Vmax)/(2.**R))
    return valoresDecisao, niveisQuantificacao


def quantificacao(sinalAmostrado, NQ, VD):
    sinalQuantificado = np.zeros(len(sinalAmostrado))
    aux = np.zeros(len(sinalAmostrado))
    for a in range(len(sinalAmostrado)):
        indice = sinalAmostrado[a] < VD
        indiceTrue = np.nonzero(indice)
        aux[a] = indiceTrue[0][0]
        sinalQuantificado[a] = NQ[aux[a]-1]

    return sinalQuantificado , aux


R = 3
Vmax = 1

VD,NQ=createTable(R,Vmax)

print ("Niveis de Quantificação : " + str(NQ))
print ("Valores de Decisão : " + str(VD))

SinalRampa=np.arange(-1,1,0.01)

potencia = potenciaSinal(SinalRampa)
SQ,IQU=quantificacao(SinalRampa , NQ, VD)

print ("Potencia do sinal: " + str(potencia))
print ("sinalQuantificado: " + str(SQ))
print ("Indices de Quantificação utilizados: " + str(IQU))

T=np.arange(0,len(SQ))
plt.grid(True)
plt.plot(T,SQ, label='SinalQuantificado')
plt.plot(T,SinalRampa, label='SinalRampa')
plt.legend(loc='lower right')
plt.show()
