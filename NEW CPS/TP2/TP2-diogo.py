# -*- coding: utf-8 -*-
import numpy as np

R = 3
Vmax = 1

def createTable(R, Vmax):
    valoresDecisao = np.arange(-Vmax , Vmax+((2.*Vmax)/(2.**R)) , (2.*Vmax)/(2.**R))
    niveisQuantificacao = np.arange(-Vmax+(Vmax/(2.**R)) , Vmax , (2.*Vmax)/(2.**R))
    return valoresDecisao, niveisQuantificacao


x,y=createTable(R,Vmax)

print "Niveis de Quantificação : " + str(y)
print "Valores de Decisão : " + str(x)


def quantificacao(sinalAmostrado, NQ, VD):
    sinalresultante = np.zeros(len(sinalAmostrado))
    for a in sinalAmostrado:
        indice = a < VD
        indice = indice*1.
