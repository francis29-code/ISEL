# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:49:31 2017

@author: joao_
"""
from PIL import Image
import numpy as np
from heapq import heappush, heappop, heapify
from time import time
from os import path
from scipy import stats
import cv2
import matplotlib.pyplot as plt


# Função que gera uma tabela com o código binário para cada símbolo de um dado
# conjunto, usando o método de Huffman. Esta função tem como parâmetros de
# entrada um conjunto de símbolos e as suas probabilidades (ou em alternativa
# é usado o número de ocorrências de cada símbolo, dado pelo seu histograma).

def gera_huffman(simb,ocurr):
    nOcorrencias = ocurr.astype(int)
    # -> [simbolos, ocorrências]
    array_zipado = zip(simb,nOcorrencias)
    array_ordenado = sorted(array_zipado, key=lambda tup: tup[1])
    # -> [ocorrências, [simbolos, binário]]
    array = [[ocorrencias,[simbolo, ""]] for simbolo, ocorrencias in array_ordenado]
    array_sem_zeros = []
    # Retirar as entradas do array que têm 0 ocorrências
    for i in range(len(array)):
        if array[i][0] != 0:
            array_sem_zeros.append(array[i])
    # Colocar as frequências num array a parte para a descodificação
    frequencias = []
    for i in range(len(array_sem_zeros)):
        frequencias.append(array_sem_zeros[i])

    array_final = []
    while len(array_sem_zeros) > 1:
        menor_ocorrencia = heappop(array_sem_zeros)
        maior_ocorrencia = heappop(array_sem_zeros)
#        print "menor: ", menor_ocorrencia, "maior: ", maior_ocorrencia

        for i in menor_ocorrencia[1:]:
            i[1] = '1' + i[1]
        for i in maior_ocorrencia[1:]:
            i[1] = '0' + i[1]

        heappush(array_sem_zeros, [menor_ocorrencia[0] + maior_ocorrencia[0]] + \
                                   menor_ocorrencia[1:] + maior_ocorrencia[1:])

    array_final = sorted(heappop(array_sem_zeros)[1:])
    return array_final, frequencias

# Função codifica que dada uma mensagem (sequência de símbolos) e a tabela do
# gerador de Huffman, retorne uma sequência de bits com a mensagem codificada.

def codifica(simb_seq, tabela):

    array_out = []
    pixeis = list(simb_seq)
    tabela_dict = dict(tabela)

    for i in pixeis:
        if i in tabela_dict:
            array_out.append(tabela_dict[i])

    return array_out

# Função escrever que dada uma sequência de bits (mensagem codificada) e o nome
# do ficheiro, escreva a sequência de bits para o ficheiro.

def escrever(mensagem, file_name):
    array_sem_plicas = ''.join(mensagem)
    array = list(map(int,array_sem_plicas))

    bits_adicionados = 0
    while (len(array) % 8) != 0:
        array.append(0)
        bits_adicionados += 1

    array = np.array(array)
    array_reshaped = array.reshape(-1,8)
    # np.packbits -> Conversão de binário para inteiros
    array_inteiros = np.packbits(array_reshaped)
    # Conversão de inteiros para caracteres
    array_char = map(chr, array_inteiros)
    # Inserir os bits adicionais no inicio do ficheiro
    array_char.insert(0,str(bits_adicionados))

    with open(file_name, 'wb') as ficheiro:
        for i in array_char:
            ficheiro.write(i)

# Função que dado o nome do ficheiro, lê uma sequência de bits (mensagem
# codificada) contida no ficheiro.

def ler(file_name):

    with open(file_name, 'rb') as ficheiro:
        data = ficheiro.read()

    array_chars = data[1:]
    novo_array = map(ord,array_chars)

    array_binario = bin_converter(novo_array)
    array_binario = ''.join(array_binario)

    return array_binario

# Função que dada uma sequência de bits (mensagem codificada) e a tabela com o
# código de Huffman retorne uma sequência de símbolos (mensagem descodificada).

def descodifica(array_in, tabela):

    # Trocar as keys por os values
    tabela_dict = dict((i[1], i[0]) for i in tabela)

    index = 0
    array_out = []

    while index < len(array_in):
        for key in tabela_dict:
            if array_in[index : index + len(key)] == key:
                array_out.append(tabela_dict[key])
                index += len(key)
                break

    return array_out

###############################################################################
#                       Funções Auxiliares
###############################################################################

# Função que converte um array de inteiros em um array de binários
def bin_converter(array):

    array_bin = []
    for i in array:
        array_bin.append(format(i, '08b'))

    return array_bin

# Função que retorna a entropia com base nas probabilidades de cada simbolo.
def entropia(frequencias):

    probabilidades = [i[0] for i in frequencias]
    entropia = stats.entropy(probabilidades,None,2.)

    return entropia

# Função que retorna o número médio de bits por símbolo.
def nBits_simbolo(tabela):
    total = sum([i[0] for i in tabela])
    numBits = 0

    for i in range(len(tabela)):
        probs = float(tabela[i][0])/float(total)
        comp = len(tabela[i][1][1])
        numBits += probs * comp

    return numBits
# Função que retorna a eficiência com base na entropia e no nº médio bits
def eficiencia(entropia, nMedioBits):
    return float(entropia) / float(nMedioBits)

if __name__== "__main__":

    file_name = "ficheiro.txt"
    image_name = "data/Lena.tif"


    # Leitura da imagem pretendida e conversão para tons de cinzento
    img = cv2.imread(image_name, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    shape = img.shape

    # Converte a imagem (matriz) numa sequência de números (array)
    img_in = img.ravel()

    # Calculo do histogram
    h, bins, patches = plt.hist(img_in,256,[0,256])

    # Geração do código de Huffman
    t0 = time()
    codigo_huff, frequencias = gera_huffman(np.arange(0,256),h)
    t1 = time()
    print "Codigo Huffman time: ", t1-t0

    # Codificação da imagem usando o codigo de Huffman
    t2 = time()
    codificacao = codifica(img_in, codigo_huff)
    t3 = time()
    print "Codificacao time: " , t3-t2

    # Escrita da imagem codificada num ficheiro de texto
    t4 = time()
    escrever(codificacao, file_name)
    t5 = time()
    print "Escrita no ficheiro time: " , t5 - t4

    # Leitura do ficheiro
    t6 = time()
    array_bits = ler(file_name)
    t7 = time()
    print "leitura time: ", t7 - t6

    # Descodificador de Huffman
    t8 = time()
    img_out = descodifica(array_bits, codigo_huff)
    t9 = time()
    print "Desodificador time: ", t9-t8
    print "Time total: ", t9 - t0

    # Gravação da imagem
    img = np.array(img_out).reshape(shape)
    cv2.imwrite('data/lena_out.tif',img)

    entropia = entropia(frequencias)
    nBits_simb = nBits_simbolo(frequencias)
    eficiencia = eficiencia(entropia, nBits_simb)

    plt.show()
    cv2.waitKey(0)
    plt.close("all")
    cv2.destroyAllWindows()
