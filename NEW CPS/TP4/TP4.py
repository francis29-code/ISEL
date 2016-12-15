# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
import sys
import pylab as pylab
import time

start_time = time.time()

caminho = str(sys.path[0])+"\\"

def codigoPRZ(arrayBits,P,A):
    #sinal codificado, numero de amostras por bit, amplitude do codigo
