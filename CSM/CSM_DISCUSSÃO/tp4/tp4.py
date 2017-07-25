# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 11:51:13 2017

@author: joao_
"""
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from time import time
import matplotlib.patches as mpatches
from scipy import stats
from pylab import *
'''
    1. Considerar que cada frame é uma intra-frame (I). Pode usar o codificador do
    trabalho anterior ou usar o codificador já disponível:
'''

def exercicio1(imagens, qualidade):
#        print ""
        taxa_comp, snr, entropias, energias = codificacao1(imagens, qualidade)
#        print "Taxa de Compressão:"
#        print taxa_comp
#        print ""
#        print "Relação Sinal-Ruído:"
#        print snr
#        print ""
#        print "Entropia:"
#        print entropias
#        print ""
#        print "Energia:"
#        print energias
        frames = np.arange(1,12)
        
        contexto = "ex1/graficos/"
#        plt.title("SNR")
#        plt.plot(frames , snr, 'r', label="Codificador 1")
#        plt.xlabel("Frames")
#        plt.ylabel("SNR")
#        plt.grid(color='b', linestyle='-', linewidth=0.5)
#        plt.savefig(contexto + "SNR.png")
# 
#        plt.title("Taxa de Compressao")
#        plt.plot(frames,taxa_comp, 'r', label = "Codificador 1")
#        plt.xlabel("Frames")
#        plt.ylabel("Taxa compressao")
#        plt.grid(color='b', linestyle='-', linewidth=0.5)
#        plt.savefig(contexto + "Taxas.png")
#        
#        plt.title("Entropia")
#        plt.plot(frames,entropias, 'r', label = 'Codificador 1')
#        plt.xlabel("Frames")
#        plt.ylabel("Entropia")
#        plt.grid(color='b', linestyle='-', linewidth=0.5)
#        plt.savefig(contexto + "Entropia.png")
#        
        plt.title("Energia")
        plt.plot(frames,energias, 'r', label = 'Codificador 1')
        plt.xlabel("Frames")
        plt.ylabel("Energia")
        plt.grid(color='b', linestyle='-', linewidth=0.5)
        plt.savefig(contexto + "Energia.png")
        

def codificacao1(imagens, qualidade):
    
    taxa_comp = []
    snr = []
    entro = []
    energ = []
    
    for img in imagens:
        
        # Leitura das imagens
        nome_img_original = "data/" + str(img) + ".tiff"
        x_img = cv2.imread(nome_img_original, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        array_img_original = np.array(x_img)
        
        # Codificação das imagens para uma qualidade pre-definida utilizando o
        # codificador JPEG do cv2
        nome_img_guardada = "ex1/" + str(qualidade) + "_" +  str(img) + ".jpeg"
        cv2.imwrite( nome_img_guardada , x_img,(cv2.IMWRITE_JPEG_QUALITY,qualidade))
        
        # Leitura das imagens gravadas
        img_guardada = cv2.imread(nome_img_guardada, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        array_img_guardada = np.array(img_guardada)
        
        # Taxa de Compressão
        taxa_comp.append(taxa_compressao(nome_img_original,nome_img_guardada))
        
        # Relação Sinal Ruído
        snr.append(SNR(array_img_original,array_img_guardada))
        
        # Entropia
        entro.append(entropia(img_guardada))
        
        # Energia média por píxel
        energ.append(energia(img_guardada)) 
    
    return taxa_comp, snr, entro, energ
    
'''
2. Considerar que cada frame à excepção da primeira são inter-frames (P),
ou seja, todos os macroblocos são do tipo (P). Neste codificador deve criar as
P-frames, que são a diferença entre a frame a codificar e a I-frame, sem
compensação de movimento. Visualize a P-frame (ou seja a imagem a transmitir).
'''

def exercicio2(imagens, qualidade):
    # Codificação 
    t0cod = time()
    codificacao2(imagens,qualidade)
    t1cod = time()
    tempoCodificacao = t1cod - t0cod
    
    # Descodificação
    t0desc = time()
    taxa_comp, snr, entropias, energias = descodificacao2(imagens,qualidade)
    t1desc = time()
    tempoDescodificacao = t1desc - t0desc
    
#    print "Tempo de Codificação"
#    print round(tempoCodificacao,3)
#    print ""
#    print "Tempo de Descodificação"
#    print round(tempoDescodificacao,3)
#    print ""
#    print "Taxa de Compressão:"
#    print taxa_comp
#    print ""
#    print "Relação Sinal-Ruído:"
#    print snr
#    print ""
#    print "Entropia:"
#    print entropias
#    print ""
#    print "Energia:"
#    print energias
#    
    contexto = "ex2/graficos/"
    frames = np.arange(1,12)
    
#    plt.title("Signal-to-noise ratio")
#    plt.plot(frames , snr, 'g', label = "codificador 2")
#    plt.xlabel("Frames")
#    plt.ylabel("SNR")
#    plt.grid(color='b', linestyle='-', linewidth=0.5)
#    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
#    plt.savefig(contexto + "SNR.png")
    
#    plt.title("Taxa de Compressao")
#    plt.plot(frames,taxa_comp, 'g', label = "Codificador 2")
#    plt.xlabel("Frames")
#    plt.ylabel("Taxa compressao")
#    plt.grid(color='b', linestyle='-', linewidth=0.5)
#    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
#    plt.savefig(contexto + "Taxas.png")
    
#    plt.title("Entropia")
#    plt.plot(frames,entropias, 'g', label = 'Codificador 2')
#    plt.xlabel("Frames")
#    plt.ylabel("Entropia")
#    plt.grid(color='b', linestyle='-', linewidth=0.5)
#    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
#    plt.savefig(contexto + "Entropia.png")
#    
    plt.title("Energia")
    plt.plot(frames,energias, 'g', label = 'Codificador 2')
    plt.xlabel("Frames")
    plt.ylabel("Energia")
    plt.grid(color='b', linestyle='-', linewidth=0.5)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
    plt.savefig(contexto + "Energia.png")
    
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()

# Função que permite realizar a codificação utilizando o segundo método do enunciado  
def codificacao2(imagens,qualidade):
    
    # Leitura da iFrame
    nome_iFrame = "data/" + imagens[0] + ".tiff"
    i_frame = cv2.imread(nome_iFrame, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    
    # Gravação da iFrame para uma qualidade pré-definida no formato JPEG
    novo_nome = "ex2/codificacao/" + imagens[0] + ".jpeg"
    cv2.imwrite( novo_nome , i_frame,(cv2.IMWRITE_JPEG_QUALITY,qualidade))
    
    for img in range(1,len(imagens)):
        
        # Leitura de cada pFrame
        nomes = "data/" + imagens[img] + ".tiff"
        p_frame = cv2.imread(nomes, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
        # Calculo da diferença entre a pFrame atual e a iFrame
        dif = p_frame.astype(float) - i_frame.astype(float) + 128.
        
        nome_guardada = "ex2/codificacao/" + imagens[img] + ".jpeg"
        cv2.imwrite( nome_guardada , dif,(cv2.IMWRITE_JPEG_QUALITY,qualidade))
    
# Função que permite realizar a descodificação utilizando o segundo método do enunciado       
def descodificacao2(imagens, qualidade):
  
    taxa_comp = []
    snr = []
    entro = []
    energ = []
    
    i_frame = cv2.imread("ex2/codificacao/" + imagens[0] + ".jpeg", cv2.CV_LOAD_IMAGE_GRAYSCALE)
    cv2.imwrite( "ex2/descodificacao/" + imagens[0] + ".jpeg" , i_frame,(cv2.IMWRITE_JPEG_QUALITY,qualidade))
    
    for img in range(1,len(imagens)):
        # Leitura das p frames
        p_frame = cv2.imread("ex2/codificacao/" + imagens[img] + ".jpeg", cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
        # Soma das p frames com a i frame
        imgDesc = (i_frame.astype(float) + (p_frame.astype(float))) - 128.
        
        # Gravação das imagens descodificadas
        cv2.imwrite( "ex2/descodificacao/" + imagens[img] + ".jpeg" , imgDesc,(cv2.IMWRITE_JPEG_QUALITY,qualidade))
    
    for img in range(0,len(imagens)):
        
        # Leitura da sequência de imagens originais
        nome_img_original = "data/" + imagens[img] + ".tiff"
        img_original = cv2.imread(nome_img_original, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
        # Leitura das imagens descodificadas
        nome_img_descodificada = "ex2/descodificacao/" + imagens[img] + ".jpeg"
        img_descodificada = cv2.imread(nome_img_descodificada, cv2.CV_LOAD_IMAGE_GRAYSCALE)
 
        # Taxa de Compressão
        taxa_comp.append(taxa_compressao(nome_img_original,nome_img_descodificada))
        
        # Relação Sinal Ruído
        snr.append(SNR(img_original,img_descodificada))
        
        # Entropia
        entro.append(entropia(img_descodificada))
    
        # Energia média por píxel
        energ.append(energia(img_descodificada)) 
        
    return taxa_comp, snr, entro, energ

"""
3. Considerar que cada frame à excepção da primeira são inter-frames (P).
Neste codificador deve implementar a predição da frame a codificar com base na
I-frame fazendo a compensação de movimento. A frame a transmitir é a diferença
entre a frame a codificar e a sua predição. Sugere-se a construção de três funções:

    3.1. uma função para fazer a medição do erro absoluto médio entre dois blocos
         (tamanho 16 x 16);
    3.2. uma função que faça uma pesquisa (pode escolher a full-search ou outra)
         do bloco da frame a codificar numa janela de pesquisa (-15 a +15) da I-frame;
    3.3. uma função que percorra os blocos da frame a codificar e construa a frame predita;
    
Visualizar a frame predita, e a frame diferença, bem como os vectores de movimento
(use a função pylab.quiver para o efeito).
"""

def exercicio3(imagens, qualidade):
    t0cod = time()
    vetores = codificacao3(imagens, qualidade)
    t1cod = time()
    tempoCodificacao = t1cod - t0cod
    
    t0desc = time()
    taxa_comp , snr, entro, energ = ex3_descodificacao(imagens, vetores, qualidade)
    t1desc = time()
    tempoDescodificacao = t1desc - t0desc
    
    print "Tempo de Codificação"
    print round(tempoCodificacao,3)
    print ""
    print "Tempo de Descodificação"
    print round(tempoDescodificacao,3)
    print ""
    print "Taxa de Compressão:"
    print taxa_comp
    print ""
    print "Relação Sinal-Ruído:"
    print snr
    print ""
    print "Entropia:"
    print entro
    print ""
    print "Energia:"
    print energ
    
    contexto = "ex3/graficos/"
    frames = np.arange(2,12)
    
#    plt.title("Signal-to-noise ratio")
#    plt.plot(frames , snr, 'b', label = "codificador 3")
#    plt.xlabel("Frames")
#    plt.ylabel("SNR")
#    plt.grid(color='b', linestyle='-', linewidth=0.5)
#    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
#    plt.savefig(contexto + "SNR.png")
    
#    plt.title("Taxa de Compressao")
#    plt.plot(frames,taxa_comp, 'b', label = "Codificador 3")
#    plt.xlabel("Frames")
#    plt.ylabel("Taxa compressao")
#    plt.grid(color='b', linestyle='-', linewidth=0.5)
#    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
#    plt.savefig(contexto + "Taxas.png")
    
#    plt.title("Entropia")
#    plt.plot(frames,entro, 'b', label = 'Codificador 3')
#    plt.xlabel("Frames")
#    plt.ylabel("Entropia")
#    plt.grid(color='b', linestyle='-', linewidth=0.5)
#    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
#    plt.savefig(contexto + "Entropia.png")
#    
    plt.title("Energia")
    plt.plot(frames,energ, 'b', label = 'Codificador 3')
    plt.xlabel("Frames")
    plt.ylabel("Energia")
    plt.grid(color='b', linestyle='-', linewidth=0.5)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
    plt.savefig(contexto + "Energia.png")
    
def codificacao3(imagens,qualidade):
    print "CODIFICAÇÃO"
    nome = "data/" + imagens[0] + ".tiff"
    i_frame = cv2.imread(nome, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    
    cv2.imwrite( "ex3/codificacao/" + imagens[0] + ".jpeg", i_frame, (cv2.IMWRITE_JPEG_QUALITY,qualidade))
    
    altura, largura = i_frame.shape
    index = 0
    vetor = np.zeros((((altura*largura)/(16*16))*2)*len(imagens)) 
    vetor = vetor.reshape((altura*largura)/(16*16),len(imagens)*2)
    
    for img in range(1, len(imagens)):
        
        nomes_pFrame = "data/" + imagens[img] + ".tiff"
        p_frame = cv2.imread(nomes_pFrame, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
        img_codificada , vetores = predicao_movimento(i_frame, p_frame)
        
        nome_img_guardada = "ex3/codificacao/" + imagens[img] + ".jpeg"
        cv2.imwrite( nome_img_guardada , img_codificada,(cv2.IMWRITE_JPEG_QUALITY,qualidade))
        
#        ''' Vizualizar os vetores de movimento '''
#        plt.figure(img)
#        blocosX = largura/16.
#        blocosY = altura/16.
#        
##         As coordenadas x e y da localização das setas
#        X, Y = np.meshgrid(np.arange(0,blocosX)*16,np.arange(0,blocosY)*16)
#        Y[::-1]
#        
##         Dar o componente x e y dos vetores das setas
#        U = ([vector[0] for vector in vetores])
#        V = [vector[1] for vector in vetores]
#
#        quiver(X,Y,U,V, angles = 'xy', scale_units = 'xy' , scale=1)
#        plt.gca().invert_yaxis()
#    
#        nome_vetores =  "ex3/vetores/"+ str(img) + ".png" 
#        plt.savefig(nome_vetores)
        
        vetor[:,index] = vetores[:,0]
        vetor[:,index +1 ] = vetores[:,1]
        index += 2
        
    return vetor
        
def ex3_descodificacao(imagens, vetores, qualidade):
    
    print "DESCODIFICAÇÃO"
    nome = "data/" + imagens[0] + ".tiff"
    i_frame = cv2.imread(nome, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    idx = 0
    
    taxa_comp = []
    snr = []
    entro = []
    energ = []
    
    for img in range(1,len(imagens)):
        
        vetor = vetores[: , idx:idx+2]
        idx += 2
        
        nome = "ex3/codificacao/" + imagens[img] + ".jpeg"
        p_frame = cv2.imread(nome, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
        altura , largura = p_frame.shape
        array_zeros = np.zeros(altura * largura)
        array_zeros = array_zeros.reshape(altura, largura)
        
        count = 0
        for col in np.arange(0,altura,16):
            for lin in np.arange(0,largura,16):
                array_zeros[col:col+16 , lin:lin+16] = i_frame[col + vetor[count,0] : col + vetor[count,0] + 16 , lin + vetor[count,1]:lin+vetor[count,1]+16]
                count += 1
                
        img_descodificada = (array_zeros.astype(float) + (p_frame.astype(float))) - 128.
        
        '''Guardar as imagens '''
        nome_img_guardada = "ex3/descodificacao/" + imagens[img] + ".jpeg"
        cv2.imwrite( nome_img_guardada , img_descodificada,(cv2.IMWRITE_JPEG_QUALITY,qualidade))
        
        
    for img in range(1,len(imagens)):
        
        nome_original = "data/" + imagens[img] + ".tiff"
#        print "Ficheiro", imagens[img], ":"
        img_original = cv2.imread(nome_original, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
        nome_img_guardada = "ex3/descodificacao/" + imagens[img] + ".jpeg"
        img_guardada = cv2.imread(nome_img_guardada, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
#        nome_img_codificada = "ex3/codificacao/" + imagens[img] + ".jpeg"
        
        # Taxa de Compressão
        taxa_comp.append(taxa_compressao(nome_original, nome_img_guardada))
        
        # Relação Sinal Ruído
        snr.append(SNR(img_original,img_guardada))
        
         # Entropia
        entro.append(entropia(img_guardada))
        
        # Energia média por píxel
        energ.append(energia(img_guardada)) 
        
    return taxa_comp, snr, entro, energ
          
def predicao_movimento(i_frame, p_frame):
    
    idx = 0
    altura , largura = i_frame.shape
    array_final = np.zeros(altura * largura)
    array_final = array_final.reshape(altura, largura)

    vetores_mov = np.zeros(((altura*largura)/(16*16))*2)
    vetores_mov = vetores_mov.reshape((altura*largura)/(16*16),2)
    
    for col in np.arange(0,altura,16):
        for lin in np.arange(0,largura,16):
            
            # Janela de pesquisa [-15, 15]
            ini = [col - 15, lin - 15]
            fim = [(col + 16) + 15, (lin + 16) + 15]
            
            # Criar bolo 16x16
            blocoP_16x16 = p_frame[col:col+16, lin:lin+16]
            
            if (ini[0] < 0):
                 ini[0] = 0
            if (ini[1] < 0):        
                 ini[1] = 0
            if (fim[0] > altura):
                 fim[0] = altura
            if (fim[1] > largura): 
                 fim[1] = largura
            
            janela_pesquisa = i_frame[ini[0]:fim[0],ini[1]:fim[1]]
             
            bloco, coluna, linha = full_search(blocoP_16x16, janela_pesquisa, ini[0], ini[1], col, lin)
            vetores_mov[idx] = coluna , linha 
            array_final[col:col+16,lin:lin+16] = bloco
            idx += 1
                   
    codificado = p_frame.astype(float) - array_final.astype(float) + 128.
    return  codificado , vetores_mov
        
def full_search(bloco_16x16, janela_pesquisa, janela_x, janela_y, Pframex, Pframey):
    
    altura, largura = janela_pesquisa.shape
    minimo = 10**20 
    array = 0
    coluna = 0
    linha = 0
    
    for i in np.arange(altura-15): 
        for j in np.arange(largura-15):
            
            bloco = janela_pesquisa[i:i+16, j:j+16]
            
            # Função que permite realizar o calculo do erro absoluto médio
            # entre ambos os blocos
            diff = MAE(bloco_16x16,bloco)
            
            if (diff < minimo):
                coluna = i
                linha = j
                array = bloco
                minimo = diff
       
    x = janela_x + coluna
    y = janela_y + linha 
    
    coordx = x - Pframex
    coordy = y - Pframey

    return array, coordx, coordy 
        
''' FUNÇÕES AUXILIARES '''
def MAE(bloco1,bloco2):    
    return np.sum(abs((1.0 * bloco1) - (1.0 * bloco2)))
    
def taxa_compressao(original,descodificada):
    sizeO = os.path.getsize(original)
    sizeA = os.path.getsize(descodificada)
    ratio = float(sizeO)/float(sizeA)

    return round(ratio,2)
    
def SNR(original,descodificada):
    imageO = original.ravel()
    noise = original.astype(float) - descodificada.astype(float)
    imageA = noise.ravel()

    pOriginal = np.sum(imageO**2.)
    pdescodificada = np.sum(imageA**2.)
    SNR = 10*np.log10(pOriginal/pdescodificada)

    return round(SNR,2)

def entropia(imagem):

    hist,bins = np.histogram(imagem.ravel(),256,[0,256])
    tamanho_hist = sum(hist) 

    prob = [float(h)/tamanho_hist for h in hist] 
    entropia = -sum([p*np.log2(p) for p in prob if p != 0])
    
    return round(entropia, 2)
    
def entropias(frequencias):
    
    probabilidades = [i[0] for i in frequencias]
    entropia = stats.entropy(probabilidades,None,2.)
     
    return entropia
    
def energia(imagem):
    altura, largura = imagem.shape
    energia = (np.sum(imagem)**2)/(altura*largura)
    return energia

if __name__ == "__main__":
    imagens = []
    qualidade = 75
    
    for i in range(1,12):
        imagens.append("bola_" + str(i))
        
    
    exercicio1(imagens, qualidade)
    exercicio2(imagens, qualidade)
    exercicio3(imagens, qualidade)
    
        
    