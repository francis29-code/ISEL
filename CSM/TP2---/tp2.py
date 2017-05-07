import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import sys
import os
from heapq import heappush, heappop, heapify

path = str(sys.path[0])+"\\"

def gera_huffman(simb,ocurr):
    nOcorrencias = ocurr.astype(int)
    # -> [simbolos, ocorrências]
    array_zipado = zip(simb,nOcorrencias)
    array_ordenado = sorted(array_zipado, key=lambda tup: tup[1])
    # -> [ocorrências, [simbolos, binário]]
    array = [[ocorrencias,[simbolo, ""]] for simbolo, ocorrencias in array_ordenado]
    array_sem_zeros = []
    frequencias = []
    # Retirar as entradas do array que têm 0 ocorrências
    for i in range(len(array)):
        if array[i][0] != 0:
            array_sem_zeros.append(array[i])
            frequencias.append(array[i])

    array_final = []
    print("Array sem Zeros: {}".format(array_sem_zeros) + "\n")
    while len(array_sem_zeros) > 1:
        menor_ocorrencia = heappop(array_sem_zeros)
        maior_ocorrencia = heappop(array_sem_zeros)
        print("menor: {}  \nmaior: {} ".format(menor_ocorrencia,maior_ocorrencia))

        for i in menor_ocorrencia[1:]:
            i[1] = '1' + i[1]
        for i in maior_ocorrencia[1:]:
            i[1] = '0' + i[1]

        heappush(array_sem_zeros, [menor_ocorrencia[0] + maior_ocorrencia[0]] + \
                                   menor_ocorrencia[1:] + maior_ocorrencia[1:])

    array_final = sorted(heappop(array_sem_zeros)[1:])
    return array_final, frequencias


if __name__ == "__main__":
    a = np.array([1,2,3,4])
    b = np.array([4,3,2,1])

    array,freq = gera_huffman(a,b)
    print("\n"+str(array))

    # for i in array:
    #     print(i)
