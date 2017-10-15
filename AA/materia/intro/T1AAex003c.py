# -*- coding: latin-1 -*-
import numpy as np
from matplotlib import pyplot as plt
#representar vers�o amostrada de sinos�ide
t=np.linspace(-1,2,1000) #1000pts equi-espa�ados entre [-1,2]
fc=1 #frequ�ncia da sinos�ide
x_t=np.cos(2*np.pi*fc*t) #fc Hz
N=10 #n� amostras segundo (N=fs, freq. de amostragem)
#tempo discreto (T=1/fs-> amostras de 0.1 em 0.1 segundos)
n=np.arange(-10,20) #[-1xN,2xN]
x_n=np.cos(2*np.pi*fc*n/N)
plt.plot(t,x_t,':b',lw=1)
plt.stem(n*1./N,x_n,'r')
plt.axis([-1,2,-1.05,1.05])  #eixos 
plt.grid('on')               #grelha
plt.xlabel(r'$t$ (segundos)'),plt.ylabel('amplitude')
plt.title(r'$x(t)=cos(2\pi t)\quadx[n]=cos(2\pi\frac{n}{10})$')
plt.xticks(np.arange(-1,2.1,.5))  #intervalos no x = 1/2
plt.yticks(np.arange(-1,1.1,.25))  #intervalos no y = 1/4
plt.savefig('../figs/T1AAex003c.png') #guardar  em ficheiro ".png"
                                  #(na directoria "../figs/")