# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt


#-------------------Funções-------------------
#cria um sinal em rampa como por exemplo y=x
def potenciaSinal(sinalAmostrado):
    potencia = (1./len(sinalAmostrado))*np.sum(sinalAmostrado**2.)
    return potencia

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
    aux = np.zeros(len(sinalAmostrado))
    for a in range(len(sinalAmostrado)):
        indice = sinalAmostrado[a] < VD
        indiceTrue = np.nonzero(indice)
        aux[a] = indiceTrue[0][0]
        sinalQuantificado[a] = NQ[aux[a]-1]

    return sinalQuantificado , aux







#--------------------Vareaveis-----------------------
R = 3
Vmax = 1
SinalRampa=np.arange(-1,1,0.01)


#--------------Execução de funções-------------------
VD,NQ=createTable(R,Vmax)
SQ,IQU=quantificacao(SinalRampa , NQ, VD)
potencia = potenciaSinal(SinalRampa)


#----------------------Prints------------------------
print "------------------------------------------------------------------------"
print "Niveis de Quantificação: \n" + str(NQ)
print "------------------------------------------------------------------------"
print "Valores de Decisão: \n" + str(VD)
print "------------------------------------------------------------------------"
print "Potencia do sinal: " + str(potencia)
print "------------------------------------------------------------------------"
print "sinalQuantificado: \n" + str(SQ)
print "------------------------------------------------------------------------"
print "Indices de Quantificação utilizados: \n" + str(IQU)
print "------------------------------------------------------------------------"


#-----------------------Plots-----------------------
Tsq=np.arange(0,len(SQ))
plt.grid(True)
plt.plot(Tsq,SQ, label='SinalQuantificado')
plt.plot(Tsq,SinalRampa, label='SinalRampa')
plt.legend(loc='lower right')
plt.show()
