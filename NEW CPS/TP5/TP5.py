# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
import sys
import pylab as pylab
import time
from TP2e3 import createTable
from TP2e3 import quantificacao
from TP2e3 import codificaSinal
from TP2e3 import SNRTeorico
from TP2e3 import SNRPratico
from TP2e3 import potenciaErroQuant
from TP2e3 import erroQuantificacao
from TP2e3 import potenciaSinal
from TP2e3 import descodificaSinal
from TP2e3 import quantificacaoInversa
from TP2e3 import recordSignal
from TP3 import hamming
from TP3 import sindrome


start_time = time.time()

caminho = str(sys.path[0])+"\\"

teste=np.array([0,0,1,1])

def QPSK(arrayBits,P,Eb):
    nBits = 2
    currentPosition=0
    newArray = np.zeros(len(arrayBits)/2)
    for i in range(0,len(arrayBits),2):
        
        newArray[currentPosition]=arrayBits[]
