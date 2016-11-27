# -*- coding: utf-8 -*-
"""
Created on Mon Nov 03 16:29:52 2014

@author:    Claudia Rodrigues 41026
            Sara Machas 40567
            Ana Rodrigues 40517
"""
import numpy as np


#funcoes anteriores

def get_tabela (r,Vmax):
    n_intervalos= 2**r
    delta_v=2.*Vmax/n_intervalos
    valores_de_decisao= np.arange(-Vmax,Vmax+delta_v,delta_v)
    
    valores_de_quantificacao= np.arange(-Vmax+(delta_v/2.),Vmax,delta_v)
    
    return valores_de_decisao, valores_de_quantificacao
    
def quantificacao (x, tabela_quantificacao, tabela_decisao):
    SinalQuantificado = np.zeros(len(x))
    IndicesQ = np.zeros(len(x), dtype=np.int)
    
    for i in range(len(tabela_quantificacao)): 
        #array com true nas posicoes que pertencem ao intervalo
        valores_no_intervalo=np.where(np.logical_and(x>= tabela_decisao[i], x < tabela_decisao[i+1]))[0]
        SinalQuantificado[valores_no_intervalo]=tabela_quantificacao[i]
        IndicesQ[valores_no_intervalo]=i
        
    valores_no_intervalo=np.where(x>=tabela_decisao[-1])
    SinalQuantificado[valores_no_intervalo]=tabela_quantificacao[-1]
    IndicesQ[valores_no_intervalo]=len(tabela_quantificacao)-1
    
    valores_no_intervalo=np.where(x<=tabela_decisao[0])
    SinalQuantificado[valores_no_intervalo]=tabela_quantificacao[0]
    IndicesQ[valores_no_intervalo]=0
    
    return SinalQuantificado, IndicesQ
    

def arrayToBinario(arrayInt,R):
    stringSaida = ''
    stringFormatacao = '{0:b}'
    for i in range(len(arrayInt)):
        stringSaida += (stringFormatacao.format(int(arrayInt[i])).zfill(R))
        
    return stringSaida
 

    
def binarioToArray(string, R):
    ArraySaida = np.zeros(len(string)/R, dtype=np.int)
    for i in range(len(string)/R):
        ArraySaida[i] = int(str(string[i*R:i*R+R]),2)
    return ArraySaida
    
def ArrayToString(Array):
    StringSaida = ""
    for bit in Array:
        StringSaida += str(bit)
    return StringSaida
    
def DescodificacaoDoSinal(valoresCodificacao, arrayIndices):
    ArraySaida=np.zeros(len(arrayIndices))
    for i in range(len(arrayIndices)):
        ArraySaida[i] = valoresCodificacao[int(arrayIndices[i])]
    return ArraySaida


def SNRqdBTeorica(SinalOriginal, Vmaxq, R):
    Psinal= sum(SinalOriginal**2.)/len(SinalOriginal)
    return 6.02*R + 10*(np.log10((3*Psinal)/(Vmaxq**2)))

def SNRqdBPratica(SinalOriginal, SinalqQuantificado):
    Ruido = SinalOriginal - SinalqQuantificado
    return 10.*np.log10(sum(SinalOriginal**2)/sum(Ruido**2))  





######################## Trabalho Pratico 3 ###################################
#1)
def Hamming(sinal):
   Adicionar = (4-len(sinal)%4)%4
   sinal = np.hstack((sinal,np.ones(Adicionar)))
   sinalSaida = np.zeros((len(sinal)/4)*7)
   G = np.array([[1,0,0,0,1,1,1],[0,1,0,0,1,1,0],[0,0,1,0,1,0,1],[0,0,0,1,0,1,1]]) #array com valores inteiros
   for i in np.arange(len(sinal)/4):
        C=np.dot((sinal[i*4:((i+1)*4)]),G)%2 #dot = multiplica matrizes, e o resto da divisão por 2 torna os valores binários
        sinalSaida[i*7:(i+1)*7] =C
   return sinalSaida



#2)
def detectarCorrigirErros(SinalIn):
    sinal = np.array(SinalIn)
    sinalsaida = np.zeros((len(sinal)/7)*4)
    Ht = np.array([[1,1,1],[1,1,0],[1,0,1],[0,1,1],[1,0,0],[0,1,0],[0,0,1]])
    for i in np.arange(len(sinal)/7):
         Valor=np.dot((sinal[i*7:((i+1)*7)]),Ht)%2
         if (sum(Valor)!=0):
             index = -int(str(int(100* Valor[0]+10*Valor[1]+Valor[2])),2)
#normalmente no codigo de Hamming ficam 3 bits do sinal, 1 redundante, 1 de Sinal, e mais 2 Redundantes
#como na nossa implementação temos os 4 bits de sinal juntos e dpeois os 3 redundantes, temos que efectuar a troca do (-3) pelo (-4)
             if index==-3:
                index = -4
             elif index==-4:
                index = -3
             valorCorrecto = (sinal[i*7:((i+1)*7)][index]+1)%2
             sinal[i*7:((i+1)*7)][index] = valorCorrecto
         sinalsaida[i*4:(i+1)*4]=sinal[i*7:i*7 + 4]
    return np.array(sinalsaida,  dtype=int)
    
    
    
#3
def inserirErro(sinal,BER):
    y = 1*np.logical_xor(sinal, np.random.binomial(1,BER, len(sinal)))
    return y

def stringToArrayBin(string): #entra em string e sai em array de bits
    Array = np.ones(len(string))
    for a in np.arange(len(string)):
        Array[a] = int(string[a])
    return Array


if __name__=="__main__":                       
    fs7=8000
    t7= np.arange(fs7*1.)/fs7
    y7 = 1000*np.cos(2.0*np.pi*1008*t7)
    
    R=3
    valorMax=np.amax(abs(y7))
    #Obter as tabelas
    vD, vQ = get_tabela(R, valorMax)
    #Quantificar o sinal com as tabelas
    sinalQUantificado, indiceQ = quantificacao(y7, vQ, vD)
    #Converter os indices do sinal quantificado para dar p converter para binario
    valorBinarioCodificado = arrayToBinario(indiceQ, R)
    
    #AQUI INSEREM-SE AS NOVAS FUNCIONALIDADES
    ArrayBins = stringToArrayBin (valorBinarioCodificado)
    
    sinalHamming = Hamming(ArrayBins)
    
    sinalErro = inserirErro(sinalHamming, 0.01)


    sinalCorrigido = detectarCorrigirErros(sinalErro)
    
    simulador2 = 1 * \
    (np.logical_xor(ArrayBins, sinalCorrigido))
    print np.sum(simulador2)
    String = ArrayToString(sinalCorrigido)
    #Voltar a reconverter os indices em binario para valores decimais
    arrayDescodificado = binarioToArray(String,R)
    #Volta a obter-se as amplitudes do sinal, apartir dos indices e da tabelas de valores de quantificacao
    SinalFinal = DescodificacaoDoSinal(vQ, arrayDescodificado)         
                 
    SNR = SNRqdBPratica(y7, SinalFinal)
    print SNR          
                 
                 
                 
                 
                 
                 