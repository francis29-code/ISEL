# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt

R = 3
Vmax = 1

def createTable(R, Vmax):
    valoresDecisao = np.arange(-Vmax , Vmax+((2.*Vmax)/(2.**R)) , (2.*Vmax)/(2.**R))
    niveisQuantificacao = np.arange(-Vmax+(Vmax/(2.**R)) , Vmax , (2.*Vmax)/(2.**R))
    return valoresDecisao, niveisQuantificacao


VD,NQ=createTable(R,Vmax)

print "Niveis de Quantificação : " + str(NQ)
print "Valores de Decisão : " + str(VD)


def quantificacao(sinalAmostrado, NQ, VD):
    sinalQuantificado = np.zeros(len(sinalAmostrado))
    aux = np.zeros(len(sinalAmostrado))
    for a in range(len(sinalAmostrado)):
        indice = sinalAmostrado[a] < VD
        indiceTrue = np.nonzero(indice)
        aux[a] = indiceTrue[0][0]
        sinalQuantificado[a] = NQ[aux[a]-1]

    return sinalQuantificado , aux


SinalRampa=np.arange(-1,1,0.01)

SQ,VQ=quantificacao(SinalRampa , NQ, VD)

print "sinalQuantificado: " + str(SQ)
print "Valores de Quantificação utilizados: " + str(VQ)

T=np.arange(0,len(SQ))
plt.grid(True)

plt.plot(T,SQ, label='SinalQuantificado')
plt.plot(T,SinalRampa, label='SinalRampa')
plt.legend(loc='lower right')
plt.show()
