# -*- coding: utf-8 -*-
import numpy as np

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
        print "indice: " + str(indice)
        indiceTrue = np.nonzero(indice)
        print "indiceTrue: " + str(indiceTrue[0])
        aux[a] = indiceTrue[0][0]
        sinalQuantificado[a] = NQ[aux[a]-1]

    return sinalQuantificado , aux

SQ,VQ=quantificacao([0.3,0.6,-0.3,-.6,.8] , NQ, VD)

print "sinalQuantificado: " + str(SQ)
print "Valores de Quantificação utilizados: " + str(VQ)
