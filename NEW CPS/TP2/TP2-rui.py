import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
import sys
import pylab as pylab


def tabelas(R, Vmax):
    #sendo R o numero de bits
    #Vmax a voltagem maxima do sinal
    L = 2**R
    deltaQ = (2.*Vmax) / L

    print("T")
